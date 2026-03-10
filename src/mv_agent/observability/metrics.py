"""Success rate, latency, and performance metrics aggregation."""

import logging
from dataclasses import dataclass, field
from datetime import datetime

from ..models.schemas import TraceRecord

logger = logging.getLogger(__name__)


@dataclass
class ToolMetrics:
    """Aggregated metrics for a single tool."""
    tool_name: str
    total_calls: int = 0
    success_count: int = 0
    failure_count: int = 0
    total_latency_ms: int = 0
    min_latency_ms: int = 0
    max_latency_ms: int = 0
    total_cost_usd: float = 0.0

    @property
    def success_rate(self) -> float:
        return self.success_count / self.total_calls if self.total_calls else 0.0

    @property
    def avg_latency_ms(self) -> float:
        return self.total_latency_ms / self.total_calls if self.total_calls else 0.0

    @property
    def avg_cost_usd(self) -> float:
        return self.total_cost_usd / self.total_calls if self.total_calls else 0.0


@dataclass
class PromptMetrics:
    """Aggregated metrics for a prompt version."""
    prompt_name: str
    prompt_version: str
    total_calls: int = 0
    success_count: int = 0
    failure_count: int = 0
    avg_latency_ms: float = 0.0
    total_cost_usd: float = 0.0
    error_types: dict[str, int] = field(default_factory=dict)


class MetricsAggregator:
    """Aggregate trace records into actionable metrics.

    Usage:
        aggregator = MetricsAggregator()
        aggregator.ingest(traces)
        tool_metrics = aggregator.get_tool_metrics()
        prompt_metrics = aggregator.get_prompt_metrics()
    """

    def __init__(self):
        self._tool_metrics: dict[str, ToolMetrics] = {}
        self._prompt_metrics: dict[str, PromptMetrics] = {}
        self._traces: list[TraceRecord] = []

    def ingest(self, traces: list[TraceRecord]) -> None:
        """Ingest a batch of trace records."""
        self._traces.extend(traces)
        for trace in traces:
            self._update_tool_metrics(trace)
            self._update_prompt_metrics(trace)

    def _update_tool_metrics(self, trace: TraceRecord) -> None:
        """Update tool-level metrics from a trace."""
        if not trace.tool_name:
            return

        if trace.tool_name not in self._tool_metrics:
            self._tool_metrics[trace.tool_name] = ToolMetrics(
                tool_name=trace.tool_name,
                min_latency_ms=trace.latency_ms,
            )

        m = self._tool_metrics[trace.tool_name]
        m.total_calls += 1
        m.total_latency_ms += trace.latency_ms
        m.total_cost_usd += trace.cost_usd
        m.min_latency_ms = min(m.min_latency_ms, trace.latency_ms)
        m.max_latency_ms = max(m.max_latency_ms, trace.latency_ms)

        if trace.success:
            m.success_count += 1
        else:
            m.failure_count += 1

    def _update_prompt_metrics(self, trace: TraceRecord) -> None:
        """Update prompt-level metrics from a trace."""
        if not trace.prompt_name:
            return

        key = f"{trace.prompt_name}@{trace.prompt_version}"
        if key not in self._prompt_metrics:
            self._prompt_metrics[key] = PromptMetrics(
                prompt_name=trace.prompt_name,
                prompt_version=trace.prompt_version,
            )

        m = self._prompt_metrics[key]
        m.total_calls += 1
        m.total_cost_usd += trace.cost_usd

        if trace.success:
            m.success_count += 1
        else:
            m.failure_count += 1
            error_key = trace.error[:50] if trace.error else "unknown"
            m.error_types[error_key] = m.error_types.get(error_key, 0) + 1

        # Running average
        m.avg_latency_ms = (
            (m.avg_latency_ms * (m.total_calls - 1) + trace.latency_ms) / m.total_calls
        )

    def get_tool_metrics(self) -> dict[str, ToolMetrics]:
        """Get metrics grouped by tool."""
        return dict(self._tool_metrics)

    def get_prompt_metrics(self) -> dict[str, PromptMetrics]:
        """Get metrics grouped by prompt version."""
        return dict(self._prompt_metrics)

    def get_failure_report(self) -> list[dict]:
        """Get all failed traces with details."""
        failures = [t for t in self._traces if not t.success]
        return [
            {
                "trace_id": str(t.trace_id),
                "timestamp": t.timestamp.isoformat(),
                "tool_name": t.tool_name,
                "prompt_name": t.prompt_name,
                "prompt_version": t.prompt_version,
                "error": t.error,
                "latency_ms": t.latency_ms,
            }
            for t in failures
        ]

    def get_latency_percentiles(self, tool_name: str) -> dict[str, float]:
        """Get latency percentiles for a specific tool."""
        latencies = sorted(
            t.latency_ms for t in self._traces if t.tool_name == tool_name
        )
        if not latencies:
            return {}

        n = len(latencies)
        return {
            "p50": latencies[n // 2],
            "p90": latencies[int(n * 0.9)],
            "p95": latencies[int(n * 0.95)],
            "p99": latencies[int(n * 0.99)] if n >= 100 else latencies[-1],
        }
