from typing import Dict, Type
from .base import BaseTool
from .summary_statistics import SummaryStatisticsTool
from .missing_value_analysis import MissingValueAnalysisTool
from .csv_to_delta_tool import csv_to_delta_table

class ToolRegistry:
    """Central registry for EDA tools."""
    _registry: Dict[str, Type[BaseTool]] = {}

    @classmethod
    def register_tools(cls):
        cls._registry = {
            SummaryStatisticsTool.name: SummaryStatisticsTool,
            MissingValueAnalysisTool.name: MissingValueAnalysisTool,
            # Register CSV to Delta tool as a callable (not class-based)
            "csv_to_delta_table": csv_to_delta_table,
        }

    @classmethod
    def get_tool(cls, name: str) -> BaseTool:
        if not cls._registry:
            cls.register_tools()
        tool_cls = cls._registry.get(name)
        if not tool_cls:
            raise ValueError(f"Tool '{name}' not found.")
        return tool_cls()

    @classmethod
    def list_tools(cls):
        if not cls._registry:
            cls.register_tools()
        return list(cls._registry.keys())
