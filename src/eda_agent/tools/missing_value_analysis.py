from .base import BaseTool
import pandas as pd
from ..services.spark_service import SparkService

class MissingValueAnalysisTool(BaseTool):
    name = "missing_value_analysis"
    description = "Analyze missing values in a DataFrame."

    def run(self, data, **kwargs):
        # If data is a table name, read from Spark
        if isinstance(data, str):
            spark_service = SparkService()
            df = spark_service.spark.table(data)
            pandas_df = df.toPandas()
        else:
            pandas_df = data
        missing = pandas_df.isnull().sum().to_dict()
        return {"tool": self.name, "result": missing}
