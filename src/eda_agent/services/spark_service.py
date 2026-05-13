from pyspark.sql import SparkSession
import pandas as pd

class SparkService:
    """Abstraction for Spark/Delta operations."""
    def __init__(self):
        self.spark = SparkSession.builder.getOrCreate()

    def read_delta(self, path: str) -> pd.DataFrame:
        df = self.spark.read.format("delta").load(path)
        return df.toPandas()

