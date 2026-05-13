import mlflow
from ..services.spark_service import SparkService
from ..agents.eda_agent import EDAAgent
from ..tools.csv_to_delta_tool import csv_to_delta_table
from .init_flow import InitFlow
from .execution_flow import ExecutionFlow

class BasicEDAWorkflow:
    """
    Orchestrates the two-phase EDA workflow: InitFlow and ExecutionFlow.
    """
    def __init__(self):
        self.init_flow = InitFlow()
        self.execution_flow = ExecutionFlow()
        self.phase = "INIT"
        self.mlflow_run = None

    def initialize_from_csv(self, csv_path: str, table_name: str):
        if self.mlflow_run is None:
            self.mlflow_run = mlflow.start_run(run_name=f"EDA_{table_name}")
        mlflow.log_param("csv_path", csv_path)
        mlflow.log_param("table_name", table_name)
        result = self.init_flow.upload_csv(csv_path, table_name)
        mlflow.log_dict(result, "ingest_result.json")
        if result.get("status") == "success":
            self.phase = "EXECUTION"
        return result

    def initialize_from_delta(self, table_name: str):
        if self.mlflow_run is None:
            self.mlflow_run = mlflow.start_run(run_name=f"EDA_{table_name}")
        mlflow.log_param("table_name", table_name)
        result = self.init_flow.load_delta(table_name)
        mlflow.log_dict(result, "load_result.json")
        if result.get("status") == "success":
            self.phase = "EXECUTION"
        return result

    def execute_tools(self, tool_names):
        if self.phase != "EXECUTION":
            return {"error": "Data not loaded. Please initialize with CSV or Delta table first."}
        mlflow.log_param("tool_names", tool_names)
        result = self.execution_flow.execute(tool_names)
        mlflow.log_dict(result, "eda_results.json")
        return result
