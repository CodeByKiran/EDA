"""
Tool: csv_to_delta_tool.py
Handles CSV upload and Delta table creation, updates DatasetService.
"""
from typing import Dict
from eda_agent.services.delta_ingestion_service import DeltaIngestionService
from eda_agent.services.dataset_service import DatasetService
from pyspark.sql import SparkSession

# If using LangChain tool decorator, import it here
# from langchain.tools import tool

def csv_to_delta_table(file_path: str, table_name: str) -> Dict:
    """
    Reads a CSV, creates a Delta table (Spark or Databricks SDK fallback), updates DatasetService.
    """
    ds = DatasetService.get_instance()
    ingestion = DeltaIngestionService()
    result = ingestion.ingest_csv_to_delta(file_path, table_name)
    if result.get("status") == "success":
        ds.update_state(
            table_name=result["table_name"],
            table_path=file_path,
            table_version=result.get("table_version"),
            numeric_columns=result.get("numeric_columns", []),
            categorical_columns=result.get("categorical_columns", []),
            datetime_columns=result.get("datetime_columns", [])
        )
    return result
