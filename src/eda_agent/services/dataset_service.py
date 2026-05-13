"""
DatasetService: Centralized dataset and Delta table state management.
"""
import threading
from typing import Optional, List, Dict

class DatasetService:
    _instance = None
    _lock = threading.Lock()

    def __init__(self):
        self.reset()

    @classmethod
    def get_instance(cls):
        with cls._lock:
            if cls._instance is None:
                cls._instance = DatasetService()
            return cls._instance

    def reset(self):
        self.table_name: Optional[str] = None
        self.table_path: Optional[str] = None
        self.table_version: Optional[int] = None
        self.numeric_columns: List[str] = []
        self.categorical_columns: List[str] = []
        self.datetime_columns: List[str] = []
        self.target_column: Optional[str] = None
        self.df = None  # Optional: cached pandas df

    def update_state(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

    def get_state(self) -> Dict:
        return {
            "table_name": self.table_name,
            "table_path": self.table_path,
            "table_version": self.table_version,
            "numeric_columns": self.numeric_columns,
            "categorical_columns": self.categorical_columns,
            "datetime_columns": self.datetime_columns,
            "target_column": self.target_column
        }

    def set_dataframe(self, df):
        self.df = df

    def get_dataframe(self):
        return self.df

