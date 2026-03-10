"""Versioned prompt templates for M&V workflows."""

from .registry import PromptRegistry, prompt_registry

# Import prompt modules to trigger registration
from . import reconciliation  # noqa: F401
from . import contract_review  # noqa: F401
from . import audit_support  # noqa: F401
from . import compliance  # noqa: F401

__all__ = ["PromptRegistry", "prompt_registry"]
