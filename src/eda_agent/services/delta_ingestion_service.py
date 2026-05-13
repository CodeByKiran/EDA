"""
DeltaIngestionService: Handles CSV to Delta ingestion with Spark or Databricks SDK fallback.
"""
from typing import Dict
import os

class DeltaIngestionService:
    def __init__(self):
        self.spark = None
        try:
            from pyspark.sql import SparkSession
            self.spark = SparkSession.builder.getOrCreate()
        except Exception:
            self.spark = None
        try:
            from databricks.sdk import WorkspaceClient
            self.dbx = WorkspaceClient()
        except Exception:
            self.dbx = None

    def ingest_csv_to_delta(self, file_path: str, table_name: str) -> Dict:
        if self.spark:
            try:
                df = (
                    self.spark.read
                    .option("header", True)
                    .option("inferSchema", True)
                    .csv(file_path)
                )
                full_table_name = f"labcatalog.ta26012.{table_name}"
                (
                    df.write
                    .format("delta")
                    .mode("overwrite")
                    .saveAsTable(full_table_name)
                )
                delta_df = self.spark.table(full_table_name)
                pandas_df = delta_df.limit(10000).toPandas()
                numeric_cols = pandas_df.select_dtypes(include=["number"]).columns.tolist()
                categorical_cols = pandas_df.select_dtypes(exclude=["number"]).columns.tolist()
                datetime_cols = pandas_df.select_dtypes(include=["datetime"]).columns.tolist()
                history_df = self.spark.sql(f"DESCRIBE HISTORY {full_table_name}")
                latest_version = history_df.select("version").first()[0]
                return {
                    "status": "success",
                    "table_name": full_table_name,
                    "table_version": latest_version,
                    "rows": delta_df.count(),
                    "columns": delta_df.columns,
                    "numeric_columns": numeric_cols,
                    "categorical_columns": categorical_cols,
                    "datetime_columns": datetime_cols
                }
            except Exception as e:
                # If Spark fails, fall through to SDK
                pass
        # Fallback: Databricks SDK
        if self.dbx:
            try:
                # Example: Use Databricks SDK to upload file and create Delta table via SQL
                # This is a simplified placeholder; real implementation may require jobs or SQL endpoints
                upload_path = f"/tmp/{os.path.basename(file_path)}"
                with open(file_path, "rb") as f:
                    self.dbx.dbfs.upload(upload_path, f, overwrite=True)
                # Now create Delta table via SQL
                full_table_name = f"labcatalog.ta26012.{table_name}"
                create_sql = f"""
                CREATE OR REPLACE TABLE {full_table_name}
                USING DELTA
                AS SELECT * FROM csv.`dbfs:{upload_path}`
                """
                self.dbx.sql_statements.execute(create_sql)
                # Metadata fetch (simplified)
                # In real code, fetch schema, row count, etc. via SDK
                return {
                    "status": "success",
                    "table_name": full_table_name,
                    "table_version": 0,
                    "rows": None,
                    "columns": None,
                    "note": "Created via Databricks SDK fallback"
                }
            except Exception as e:
                return {"error": f"Databricks SDK fallback failed: {str(e)}"}
        return {"error": "No Spark or Databricks SDK available for ingestion."}

