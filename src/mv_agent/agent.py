"""Core agent orchestrator — routes tasks to tools and manages prompt execution."""

import logging
from typing import Any

from .config import config
from .tools import TOOL_REGISTRY
from .prompts import prompt_registry
from .observability.tracer import Tracer, get_trace_buffer
from .observability.cost_tracker import CostTracker
from .observability.store import TraceStore

logger = logging.getLogger(__name__)


class MVAgent:
    """M&V Specialist Agent — orchestrates tools and prompts for energy management tasks.

    Usage:
        agent = MVAgent()

        # Run a tool directly
        result = agent.run_tool("reconcile_savings", contract_id="ESPC-001", ...)

        # Render a prompt
        prompt = agent.render_prompt("reconciliation.analyze", contract_id="ESPC-001", ...)

        # Flush traces to persistent storage
        agent.flush_traces()
    """

    def __init__(self, model: str | None = None, trace_db_path=None):
        self.model = model or config.default_model
        self.cost_tracker = CostTracker()
        self.store = TraceStore(db_path=trace_db_path)
        logger.info("MVAgent initialized with model=%s", self.model)

    def run_tool(self, tool_name: str, **kwargs) -> Any:
        """Execute a registered MCP tool.

        Args:
            tool_name: Name of the tool (must be in TOOL_REGISTRY).
            **kwargs: Arguments to pass to the tool function.

        Returns:
            Tool output (typed per tool implementation).

        Raises:
            KeyError: If tool_name is not registered.
        """
        if tool_name not in TOOL_REGISTRY:
            raise KeyError(
                f"Unknown tool: {tool_name}. Available: {list(TOOL_REGISTRY.keys())}"
            )

        logger.info("Running tool: %s", tool_name)
        tool_fn = TOOL_REGISTRY[tool_name]
        return tool_fn(**kwargs)

    def render_prompt(
        self,
        prompt_name: str,
        version: str | None = None,
        **kwargs,
    ) -> str:
        """Render a prompt template with provided variables.

        Args:
            prompt_name: Registered prompt name (e.g., "reconciliation.analyze").
            version: Specific version (defaults to current default).
            **kwargs: Template variables.

        Returns:
            Rendered prompt string.
        """
        prompt = prompt_registry.get(prompt_name, version=version)
        rendered = prompt.render(**kwargs)
        logger.debug(
            "Rendered prompt %s@%s (%d chars)",
            prompt_name, prompt.version, len(rendered)
        )
        return rendered

    def list_tools(self) -> list[str]:
        """List all available tools."""
        return list(TOOL_REGISTRY.keys())

    def list_prompts(self) -> list[dict]:
        """List all registered prompts with their versions."""
        result = []
        for name in prompt_registry.list_prompts():
            versions = prompt_registry.list_versions(name)
            result.append({
                "name": name,
                "versions": [
                    {
                        "version": v.version,
                        "description": v.description,
                        "is_default": v.is_default,
                    }
                    for v in versions
                ],
            })
        return result

    def flush_traces(self) -> int:
        """Flush in-memory traces to persistent storage.

        Returns:
            Number of traces flushed.
        """
        buffer = get_trace_buffer()
        if not buffer:
            return 0

        count = len(buffer)
        self.store.save_traces(list(buffer))
        buffer.clear()
        logger.info("Flushed %d traces to store", count)
        return count

    def get_cost_summary(self) -> dict:
        """Get cost tracking summary."""
        return self.cost_tracker.get_summary()
