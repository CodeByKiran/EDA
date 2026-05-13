from ..agents.eda_agent import EDAAgent
from ..services.dataset_service import DatasetService
import mlflow

class ExecutionFlow:
    """
    Handles EDA tool execution after data is loaded.
    """
    def __init__(self):
        self.agent = EDAAgent()

    def execute(self, tool_names):
        mlflow.log_param("tool_names", tool_names)
        ds = DatasetService.get_instance()
        table_name = ds.table_name
        if not table_name:
            return {"error": "No Delta table loaded. Please initialize data first."}
        result = self.agent.run(tool_names, table_name)
        mlflow.log_dict(result, "executionflow_eda_results.json")
        return result
