from abc import ABC, abstractmethod
from typing import Dict, Any, Optional


class BaseTool(ABC):
    """Abstract base class for all tools."""

    def __init__(self, name: str, description: str = ""):
        self.name = name
        self.description = description

    @abstractmethod
    def can_handle(self, prompt: str) -> bool:
        """Check if this tool can handle the given prompt."""
        pass

    @abstractmethod
    def execute(
        self,
        prompt: str,
        context: Optional[Dict[str, Any]] = None
    ) -> Optional[str]:
        """Execute the tool with the given prompt."""
        pass

    def validate_context(self, context: Optional[Dict[str, Any]] = None) -> bool:
        """Validate if the context has required parameters."""
        return True
