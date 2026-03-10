"""Prompt version registry — stores, versions, and retrieves prompt templates."""

import logging
from dataclasses import dataclass, field
from datetime import datetime, timezone

logger = logging.getLogger(__name__)


@dataclass
class PromptVersion:
    """A single version of a prompt template."""
    name: str
    version: str
    template: str
    description: str = ""
    created_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    is_default: bool = False
    metadata: dict = field(default_factory=dict)

    def render(self, **kwargs) -> str:
        """Render the template with provided variables."""
        return self.template.format(**kwargs)


class PromptRegistry:
    """Registry for versioned prompt templates.

    Usage:
        registry = PromptRegistry()
        registry.register("reconciliation", "v1", template="...", is_default=True)
        registry.register("reconciliation", "v2", template="...")

        # Get default version
        prompt = registry.get("reconciliation")

        # Get specific version
        prompt_v1 = registry.get("reconciliation", version="v1")

        # List all versions
        versions = registry.list_versions("reconciliation")
    """

    def __init__(self):
        self._prompts: dict[str, dict[str, PromptVersion]] = {}
        self._defaults: dict[str, str] = {}

    def register(
        self,
        name: str,
        version: str,
        template: str,
        description: str = "",
        is_default: bool = False,
        metadata: dict | None = None,
    ) -> PromptVersion:
        """Register a new prompt version."""
        pv = PromptVersion(
            name=name,
            version=version,
            template=template,
            description=description,
            is_default=is_default,
            metadata=metadata or {},
        )

        if name not in self._prompts:
            self._prompts[name] = {}
            is_default = True  # First version is always default

        self._prompts[name][version] = pv

        if is_default:
            self._defaults[name] = version
            # Unset previous default
            for v in self._prompts[name].values():
                v.is_default = v.version == version

        logger.info("Registered prompt %s@%s (default=%s)", name, version, is_default)
        return pv

    def get(self, name: str, version: str | None = None) -> PromptVersion:
        """Get a prompt by name and optional version."""
        if name not in self._prompts:
            raise KeyError(f"Prompt not found: {name}")

        if version:
            if version not in self._prompts[name]:
                raise KeyError(f"Version not found: {name}@{version}")
            return self._prompts[name][version]

        default_version = self._defaults.get(name)
        if not default_version:
            raise KeyError(f"No default version set for: {name}")
        return self._prompts[name][default_version]

    def list_prompts(self) -> list[str]:
        """List all registered prompt names."""
        return list(self._prompts.keys())

    def list_versions(self, name: str) -> list[PromptVersion]:
        """List all versions of a prompt."""
        if name not in self._prompts:
            return []
        return sorted(
            self._prompts[name].values(),
            key=lambda p: p.created_at,
        )

    def set_default(self, name: str, version: str) -> None:
        """Set the default version for a prompt."""
        if name not in self._prompts or version not in self._prompts[name]:
            raise KeyError(f"Prompt version not found: {name}@{version}")
        self._defaults[name] = version
        for v in self._prompts[name].values():
            v.is_default = v.version == version

    def get_all_defaults(self) -> dict[str, PromptVersion]:
        """Get all prompts at their default versions."""
        return {name: self.get(name) for name in self._prompts}


# Global singleton
prompt_registry = PromptRegistry()
