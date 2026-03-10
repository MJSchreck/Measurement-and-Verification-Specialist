"""Tool-call and prompt tracing decorator and utilities."""

import functools
import hashlib
import json
import logging
import time
from uuid import uuid4

from ..models.schemas import TraceRecord

logger = logging.getLogger(__name__)

# In-memory trace buffer (flushed to store periodically)
_trace_buffer: list[TraceRecord] = []


def get_trace_buffer() -> list[TraceRecord]:
    """Access the in-memory trace buffer."""
    return _trace_buffer


def clear_trace_buffer() -> None:
    """Clear the in-memory trace buffer."""
    _trace_buffer.clear()


def _hash_data(data) -> str:
    """Create a SHA-256 hash of serialized data."""
    try:
        serialized = json.dumps(data, sort_keys=True, default=str)
        return hashlib.sha256(serialized.encode()).hexdigest()[:16]
    except (TypeError, ValueError):
        return "unhashable"


class Tracer:
    """Context manager for tracing a tool call or prompt execution."""

    def __init__(
        self,
        tool_name: str = "",
        prompt_name: str = "",
        prompt_version: str = "",
        model: str = "",
    ):
        self.record = TraceRecord(
            trace_id=uuid4(),
            tool_name=tool_name,
            prompt_name=prompt_name,
            prompt_version=prompt_version,
            model=model,
        )
        self._start_time = 0.0

    def __enter__(self):
        self._start_time = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        elapsed_ms = int((time.perf_counter() - self._start_time) * 1000)
        self.record.latency_ms = elapsed_ms

        if exc_type is not None:
            self.record.success = False
            self.record.error = str(exc_val)

        _trace_buffer.append(self.record)
        logger.debug(
            "Trace %s: tool=%s, latency=%dms, success=%s",
            self.record.trace_id,
            self.record.tool_name,
            elapsed_ms,
            self.record.success,
        )
        return False  # Don't suppress exceptions


def traced(tool_name: str = "", prompt_name: str = "", prompt_version: str = ""):
    """Decorator to automatically trace a tool function call.

    Usage:
        @traced(tool_name="parse_mv_report")
        def parse_mv_report(file_path: str) -> ReportData:
            ...
    """

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            with Tracer(
                tool_name=tool_name or func.__name__,
                prompt_name=prompt_name,
                prompt_version=prompt_version,
            ) as tracer:
                # Hash inputs
                tracer.record.input_hash = _hash_data(
                    {"args": args, "kwargs": kwargs}
                )

                result = func(*args, **kwargs)

                # Hash output
                tracer.record.output_hash = _hash_data(result)
                tracer.record.success = True

                return result

        return wrapper

    return decorator
