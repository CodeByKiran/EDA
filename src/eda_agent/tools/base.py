from abc import ABC, abstractmethod
from typing import Any, Dict

class BaseTool(ABC):
    """Abstract base class for all EDA tools."""
    name: str
    description: str

    @abstractmethod
    def run(self, data: Any, **kwargs) -> Dict:
        """Run the tool on the provided data and return standardized JSON output."""
        pass

