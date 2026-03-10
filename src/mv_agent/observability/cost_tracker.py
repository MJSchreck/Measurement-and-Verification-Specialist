"""Token usage and cost calculation for LLM calls."""

import logging
from dataclasses import dataclass, field

from ..config import MODELS, ModelConfig

logger = logging.getLogger(__name__)


@dataclass
class UsageRecord:
    """Single LLM usage record."""
    model: str
    input_tokens: int
    output_tokens: int
    cost_usd: float


@dataclass
class CostTracker:
    """Tracks cumulative token usage and costs across all LLM calls.

    Usage:
        tracker = CostTracker()
        cost = tracker.record_usage("claude-sonnet-4-20250514", input_tokens=1500, output_tokens=500)
        print(f"This call cost ${cost:.4f}")
        print(f"Total: ${tracker.total_cost:.4f}")
    """

    records: list[UsageRecord] = field(default_factory=list)
    total_input_tokens: int = 0
    total_output_tokens: int = 0
    total_cost: float = 0.0

    def record_usage(
        self,
        model: str,
        input_tokens: int,
        output_tokens: int,
    ) -> float:
        """Record token usage and calculate cost.

        Args:
            model: Model name (must be in config.MODELS).
            input_tokens: Number of input/prompt tokens.
            output_tokens: Number of output/completion tokens.

        Returns:
            Cost in USD for this call.
        """
        model_config = MODELS.get(model)
        if not model_config:
            logger.warning("Unknown model %s — using zero cost", model)
            model_config = ModelConfig(
                name=model, provider="unknown",
                input_cost_per_1k=0, output_cost_per_1k=0
            )

        input_cost = (input_tokens / 1000) * model_config.input_cost_per_1k
        output_cost = (output_tokens / 1000) * model_config.output_cost_per_1k
        total = input_cost + output_cost

        record = UsageRecord(
            model=model,
            input_tokens=input_tokens,
            output_tokens=output_tokens,
            cost_usd=total,
        )
        self.records.append(record)

        self.total_input_tokens += input_tokens
        self.total_output_tokens += output_tokens
        self.total_cost += total

        logger.debug(
            "Cost: model=%s, in=%d, out=%d, cost=$%.4f (total=$%.4f)",
            model, input_tokens, output_tokens, total, self.total_cost,
        )
        return total

    def get_cost_by_model(self) -> dict[str, float]:
        """Get total cost breakdown by model."""
        costs: dict[str, float] = {}
        for record in self.records:
            costs[record.model] = costs.get(record.model, 0) + record.cost_usd
        return costs

    def get_summary(self) -> dict:
        """Get a summary of all usage."""
        return {
            "total_calls": len(self.records),
            "total_input_tokens": self.total_input_tokens,
            "total_output_tokens": self.total_output_tokens,
            "total_cost_usd": round(self.total_cost, 4),
            "cost_by_model": self.get_cost_by_model(),
            "avg_cost_per_call": (
                round(self.total_cost / len(self.records), 4)
                if self.records else 0
            ),
        }
