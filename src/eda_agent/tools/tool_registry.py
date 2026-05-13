from typing import Dict
from .eda import EDA
from ..workflows.init_flow import load_delta_table

class ToolRegistry:
    """  Central registry for EDA tools.  """
    _registry = {}

    @classmethod
    def register_tools(cls):
        cls._registry = {
            "summary_statistics": EDA.summary_statistics,
            "missing_value_analysis": EDA.missing_value_analysis,
            # Register CSV to Delta tool as a callable (not class-based)
            "csv_to_delta_table": csv_to_delta_table,
            "load_delta_table": load_delta_table,
        }

    @classmethod
    def get_tool(cls, name: str):
        if not cls._registry:
            cls.register_tools()
        tool_fn = cls._registry.get(name)
        if not tool_fn:
            raise ValueError(f"Tool '{name}' not found.")
        return tool_fn

    @classmethod
    def list_tools(cls):
        if not cls._registry:
            cls.register_tools()
        return list(cls._registry.keys())
