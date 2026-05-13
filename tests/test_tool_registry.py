import pytest
from src.eda_agent.tools.tool_registry import ToolRegistry

def test_tool_registry_list():
    tools = ToolRegistry.list_tools()
    assert "summary_statistics" in tools
    assert "missing_value_analysis" in tools

def test_get_tool():
    tool = ToolRegistry.get_tool("summary_statistics")
    assert tool.name == "summary_statistics"

