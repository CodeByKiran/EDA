from ..tools.csv_to_delta_tool import csv_to_delta_table
from ..services.dataset_service import DatasetService
import mlflow

def load_delta_table(table_name: str):
    """
    Loads an existing Delta table by name and updates DatasetService.
    """
    ds = DatasetService.get_instance()
    ds.update_state(table_name=table_name)
    return {"status": "success", "table_name": table_name}

class InitFlow:
    """
    Handles data initialization: CSV upload and Delta table loading.
    """
    def upload_csv(self, csv_path: str, table_name: str):
        mlflow.log_param("csv_path", csv_path)
        mlflow.log_param("table_name", table_name)
        result = csv_to_delta_table(csv_path, table_name)
        mlflow.log_dict(result, "initflow_ingest_result.json")
        return result

    def load_delta(self, table_name: str):
        mlflow.log_param("table_name", table_name)
        result = load_delta_table(table_name)
        mlflow.log_dict(result, "initflow_load_result.json")
        return result
