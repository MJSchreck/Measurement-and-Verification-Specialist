"""Configuration management for the M&V Agent."""

import os
from pathlib import Path
from dataclasses import dataclass, field


@dataclass
class ModelConfig:
    """LLM model configuration with cost tracking."""

    name: str
    provider: str  # "anthropic" or "openai"
    input_cost_per_1k: float  # USD per 1K input tokens
    output_cost_per_1k: float  # USD per 1K output tokens
    max_tokens: int = 4096


# Model pricing as of March 2026
MODELS = {
    "claude-sonnet-4-20250514": ModelConfig(
        name="claude-sonnet-4-20250514",
        provider="anthropic",
        input_cost_per_1k=0.003,
        output_cost_per_1k=0.015,
        max_tokens=8192,
    ),
    "claude-haiku-3.5": ModelConfig(
        name="claude-3-5-haiku-20241022",
        provider="anthropic",
        input_cost_per_1k=0.001,
        output_cost_per_1k=0.005,
        max_tokens=8192,
    ),
    "gpt-4o": ModelConfig(
        name="gpt-4o",
        provider="openai",
        input_cost_per_1k=0.005,
        output_cost_per_1k=0.015,
        max_tokens=4096,
    ),
    "gpt-4o-mini": ModelConfig(
        name="gpt-4o-mini",
        provider="openai",
        input_cost_per_1k=0.00015,
        output_cost_per_1k=0.0006,
        max_tokens=4096,
    ),
}


@dataclass
class AgentConfig:
    """Global agent configuration."""

    default_model: str = field(
        default_factory=lambda: os.environ.get("MV_AGENT_MODEL", "claude-sonnet-4-20250514")
    )
    trace_db_path: Path = field(
        default_factory=lambda: Path(
            os.environ.get("MV_AGENT_TRACE_DB", str(Path.home() / ".mv_agent" / "traces.db"))
        )
    )
    log_level: str = field(
        default_factory=lambda: os.environ.get("MV_AGENT_LOG_LEVEL", "INFO")
    )
    savings_tolerance_pct: float = 5.0  # Default shortfall tolerance

    def get_model_config(self, model_name: str | None = None) -> ModelConfig:
        """Get model configuration by name, falling back to default."""
        name = model_name or self.default_model
        if name not in MODELS:
            raise ValueError(f"Unknown model: {name}. Available: {list(MODELS.keys())}")
        return MODELS[name]


# Singleton
config = AgentConfig()
