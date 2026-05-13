from ..tools.tool_registry import ToolRegistry
from ..formatters.json_formatter import JSONFormatter

class EDAAgent:
    """Agent orchestrates EDA tools via registry."""
    def __init__(self):
        self.registry = ToolRegistry
        self.formatter = JSONFormatter

    def run(self, tool_names, data):
        results = []
        for name in tool_names:
            tool_fn = self.registry.get_tool(name)
            result = tool_fn(data)
            results.append(result)
        return self.formatter.format(results)
