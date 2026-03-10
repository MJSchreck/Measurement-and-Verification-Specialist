"""SQLite-backed persistent storage for trace records and eval results."""

import json
import logging
import sqlite3
from datetime import datetime
from pathlib import Path
from uuid import UUID

from ..models.schemas import TraceRecord, EvalResult
from ..config import config

logger = logging.getLogger(__name__)


class TraceStore:
    """SQLite store for traces and eval results.

    Usage:
        store = TraceStore()  # Uses default path from config
        store.save_trace(trace_record)
        traces = store.get_traces(tool_name="parse_mv_report", limit=100)
        store.save_eval(eval_result)
    """

    def __init__(self, db_path: Path | None = None):
        self.db_path = db_path or config.trace_db_path
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        self._init_db()

    def _init_db(self) -> None:
        """Initialize database tables."""
        with sqlite3.connect(self.db_path) as conn:
            conn.executescript("""
                CREATE TABLE IF NOT EXISTS traces (
                    trace_id TEXT PRIMARY KEY,
                    timestamp TEXT NOT NULL,
                    tool_name TEXT,
                    prompt_name TEXT,
                    prompt_version TEXT,
                    model TEXT,
                    input_tokens INTEGER DEFAULT 0,
                    output_tokens INTEGER DEFAULT 0,
                    cost_usd REAL DEFAULT 0,
                    latency_ms INTEGER DEFAULT 0,
                    success INTEGER DEFAULT 1,
                    error TEXT,
                    input_hash TEXT,
                    output_hash TEXT,
                    metadata TEXT
                );

                CREATE TABLE IF NOT EXISTS eval_results (
                    eval_id TEXT PRIMARY KEY,
                    eval_name TEXT NOT NULL,
                    prompt_version TEXT,
                    passed INTEGER DEFAULT 0,
                    score REAL DEFAULT 0,
                    expected TEXT,
                    actual TEXT,
                    details TEXT,
                    trace_id TEXT,
                    timestamp TEXT NOT NULL
                );

                CREATE INDEX IF NOT EXISTS idx_traces_tool ON traces(tool_name);
                CREATE INDEX IF NOT EXISTS idx_traces_prompt ON traces(prompt_name, prompt_version);
                CREATE INDEX IF NOT EXISTS idx_traces_timestamp ON traces(timestamp);
                CREATE INDEX IF NOT EXISTS idx_evals_prompt ON eval_results(prompt_version);
                CREATE INDEX IF NOT EXISTS idx_evals_name ON eval_results(eval_name);
            """)
        logger.info("TraceStore initialized at %s", self.db_path)

    def save_trace(self, trace: TraceRecord) -> None:
        """Persist a single trace record."""
        with sqlite3.connect(self.db_path) as conn:
            conn.execute(
                """INSERT OR REPLACE INTO traces
                   (trace_id, timestamp, tool_name, prompt_name, prompt_version,
                    model, input_tokens, output_tokens, cost_usd, latency_ms,
                    success, error, input_hash, output_hash, metadata)
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                (
                    str(trace.trace_id),
                    trace.timestamp.isoformat(),
                    trace.tool_name,
                    trace.prompt_name,
                    trace.prompt_version,
                    trace.model,
                    trace.input_tokens,
                    trace.output_tokens,
                    trace.cost_usd,
                    trace.latency_ms,
                    1 if trace.success else 0,
                    trace.error,
                    trace.input_hash,
                    trace.output_hash,
                    json.dumps(trace.metadata),
                ),
            )

    def save_traces(self, traces: list[TraceRecord]) -> None:
        """Persist multiple trace records in a batch."""
        for trace in traces:
            self.save_trace(trace)

    def save_eval(self, result: EvalResult) -> None:
        """Persist an eval result."""
        with sqlite3.connect(self.db_path) as conn:
            conn.execute(
                """INSERT OR REPLACE INTO eval_results
                   (eval_id, eval_name, prompt_version, passed, score,
                    expected, actual, details, trace_id, timestamp)
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                (
                    result.eval_id,
                    result.eval_name,
                    result.prompt_version,
                    1 if result.passed else 0,
                    result.score,
                    result.expected,
                    result.actual,
                    result.details,
                    str(result.trace_id) if result.trace_id else None,
                    result.timestamp.isoformat(),
                ),
            )

    def get_traces(
        self,
        tool_name: str | None = None,
        prompt_name: str | None = None,
        prompt_version: str | None = None,
        success: bool | None = None,
        since: datetime | None = None,
        limit: int = 100,
    ) -> list[dict]:
        """Query traces with optional filters."""
        query = "SELECT * FROM traces WHERE 1=1"
        params: list = []

        if tool_name:
            query += " AND tool_name = ?"
            params.append(tool_name)
        if prompt_name:
            query += " AND prompt_name = ?"
            params.append(prompt_name)
        if prompt_version:
            query += " AND prompt_version = ?"
            params.append(prompt_version)
        if success is not None:
            query += " AND success = ?"
            params.append(1 if success else 0)
        if since:
            query += " AND timestamp >= ?"
            params.append(since.isoformat())

        query += " ORDER BY timestamp DESC LIMIT ?"
        params.append(limit)

        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = sqlite3.Row
            rows = conn.execute(query, params).fetchall()
            return [dict(row) for row in rows]

    def get_evals(
        self,
        eval_name: str | None = None,
        prompt_version: str | None = None,
        limit: int = 100,
    ) -> list[dict]:
        """Query eval results with optional filters."""
        query = "SELECT * FROM eval_results WHERE 1=1"
        params: list = []

        if eval_name:
            query += " AND eval_name = ?"
            params.append(eval_name)
        if prompt_version:
            query += " AND prompt_version = ?"
            params.append(prompt_version)

        query += " ORDER BY timestamp DESC LIMIT ?"
        params.append(limit)

        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = sqlite3.Row
            rows = conn.execute(query, params).fetchall()
            return [dict(row) for row in rows]

    def get_stats(self) -> dict:
        """Get overall database statistics."""
        with sqlite3.connect(self.db_path) as conn:
            trace_count = conn.execute("SELECT COUNT(*) FROM traces").fetchone()[0]
            eval_count = conn.execute("SELECT COUNT(*) FROM eval_results").fetchone()[0]
            success_count = conn.execute(
                "SELECT COUNT(*) FROM traces WHERE success = 1"
            ).fetchone()[0]
            total_cost = conn.execute(
                "SELECT COALESCE(SUM(cost_usd), 0) FROM traces"
            ).fetchone()[0]

            return {
                "total_traces": trace_count,
                "total_evals": eval_count,
                "success_rate": success_count / trace_count if trace_count else 0,
                "total_cost_usd": round(total_cost, 4),
            }
