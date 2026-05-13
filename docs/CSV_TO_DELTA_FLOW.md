# CSV Upload and Delta Table Ingestion Flow

## Overview
This document describes the flow for handling user-uploaded CSV data and converting it into a managed Delta table, which becomes the source of truth for all EDA tools and workflows.

## Flow Steps

1. **User Uploads CSV**
   - The user provides a CSV file path (from Unity Catalog, DBFS, or upload).

2. **CSV to Delta Table Tool**
   - The `csv_to_delta_table` tool reads the CSV using Spark, infers schema, and writes it as a Delta table in Unity Catalog.
   - Table metadata (name, version, columns) is extracted.
   - The centralized `DatasetService` is updated with the new table state.

3. **State Management**
   - All EDA tools and workflows access the current dataset state via `DatasetService`.
   - The Delta table name is used as the canonical data reference.

4. **EDA Tools Operate on Delta Table**
   - Tools (e.g., summary statistics, missing value analysis) accept a table name, read from Spark, and process the data as a pandas DataFrame.
   - This ensures consistency, scalability, and compatibility with Databricks Jobs and Model Serving.

5. **Workflow Orchestration**
   - The workflow orchestrates: CSV upload → Delta table creation → EDA tools execution.
   - All outputs are standardized as structured JSON.

## Dual-Mode Ingestion (Spark + Databricks SDK Fallback)

- The ingestion service first attempts to use Spark for CSV-to-Delta conversion.
- If Spark is unavailable (e.g., in some Databricks serving runtimes), it falls back to the Databricks SDK:
    - Uploads the CSV to DBFS using the SDK
    - Executes a SQL statement to create a Delta table from the uploaded CSV
- This ensures ingestion works both locally and in all Databricks environments.

See `delta_ingestion_service.py` for details.

## Benefits
- **Scalable**: Handles large datasets via Spark/Delta.
- **Consistent**: All tools use the same managed table.
- **Modular**: Easy to extend with new tools or workflows.
- **Production-Ready**: Compatible with Databricks Jobs, Model Serving, and Asset Bundles.

---
See `csv_to_delta_tool.py`, `dataset_service.py`, and `basic_eda_workflow.py` for implementation details.
