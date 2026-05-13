from ..services.spark_service import SparkService
from ..agents.eda_agent import EDAAgent
from ..tools.csv_to_delta_tool import csv_to_delta_table

class BasicEDAWorkflow:
    """Deterministic workflow for EDA."""
    def __init__(self, csv_path: str, table_name: str):
        self.csv_path = csv_path
        self.table_name = table_name
        self.agent = EDAAgent()

    def run(self):
        # Step 1: Ingest CSV to Delta
        ingest_result = csv_to_delta_table(self.csv_path, self.table_name)
        if "error" in ingest_result:
            return ingest_result
        # Step 2: Run EDA tools on Delta table
        tool_names = ["summary_statistics", "missing_value_analysis"]
        # Pass table name as data reference
        return self.agent.run(tool_names, ingest_result["table_name"])
