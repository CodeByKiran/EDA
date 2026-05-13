# EDA Agent DB

Production-grade, modular EDA Agent architecture for local development and Databricks deployment.

## What this includes

- Modular Python package under `src/eda_agent`
- Separation of layers: Agent, Tools, Workflows, Services, Formatters, Config
- Centralized tool registry
- ChatDatabricks LLM service wrapper
- Deterministic workflow orchestration
- Standardized JSON tool responses
- MLflow pyfunc serving model
- Databricks Asset Bundles skeleton for Jobs + Serving
- Basic unit tests

## Quick start (local)

```bash
python -m venv .venv
.venv\\Scripts\\activate
pip install -r requirements.txt
python main.py
```

## Run tests

```bash
pytest -q
```

## Databricks deployment (bundle)

```bash
databricks bundle validate
databricks bundle deploy -p DEFAULT -t lab-personal
databricks bundle run eda_agent_job -p DEFAULT -t lab-personal
```

## Environment variables

- `DATABRICKS_HOST`
- `DATABRICKS_TOKEN`
- `DATABRICKS_SERVING_ENDPOINT` (for ChatDatabricks endpoint name)
- `UC_CATALOG` (Optional)
- `UC_SCHEMA` (optional - Needed to perform read and Write Operations on the Table and Volumes )

