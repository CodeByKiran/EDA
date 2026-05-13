from .base import BaseTool
import pandas as pd
from ..services.spark_service import SparkService

class SummaryStatisticsTool(BaseTool):
    name = "summary_statistics"
    description = "Compute summary statistics for a DataFrame."

    def run(self, data, **kwargs):
        # If data is a table name, read from Spark
        if isinstance(data, str):
            spark_service = SparkService()
            df = spark_service.spark.table(data)
            pandas_df = df.toPandas()
        else:
            pandas_df = data
        summary = pandas_df.describe(include='all').to_dict()
        return {"tool": self.name, "result": summary}
