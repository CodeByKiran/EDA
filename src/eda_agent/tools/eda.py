import pandas as pd
from ..services.spark_service import SparkService

class EDA:
    @staticmethod
    def summary_statistics(data, **kwargs):
        if isinstance(data, str):
            spark_service = SparkService()
            df = spark_service.spark.table(data)
            pandas_df = df.toPandas()
        else:
            pandas_df = data
        summary = pandas_df.describe(include='all').to_dict()
        return {"tool": "summary_statistics", "result": summary}

    @staticmethod
    def missing_value_analysis(data, **kwargs):
        if isinstance(data, str):
            spark_service = SparkService()
            df = spark_service.spark.table(data)
            pandas_df = df.toPandas()
        else:
            pandas_df = data
        missing = pandas_df.isnull().sum().to_dict()
        return {"tool": "missing_value_analysis", "result": missing}

