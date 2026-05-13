# EDA_AGENT_DB Project Documentation

## Overview
This project is a production-grade, modular, and scalable AI Agent platform for automated Exploratory Data Analysis (EDA) on Databricks. It is designed to:
- Replace notebook-based EDA with reusable, testable, and deployable Python modules
- Support local development, Databricks Jobs, Model Serving, and Asset Bundles
- Enable future multi-agent expansion and enterprise-grade best practices

## High-Level Architecture

- **Agent Layer**: Orchestrates EDA tasks, interacts with LLMs, and manages workflows
- **Tool Layer**: Modular, reusable Python tools for EDA tasks (e.g., summary stats, missing value analysis)
- **Workflow Layer**: Deterministic orchestration of tool execution for reproducible EDA pipelines
- **Service Layer**: Abstractions for LLM (ChatDatabricks), Spark/Delta operations, and external integrations
- **Formatting Layer**: Standardizes tool outputs (e.g., JSON formatting)
- **Configuration Layer**: Centralizes config for jobs, serving, and deployment

## Project Structure

```
EDA_AGENT_DB/
│
├── src/
│   └── eda_agent/
│       ├── agents/         # Agent orchestration logic
│       ├── tools/          # Modular EDA tools (Python modules)
│       ├── workflows/      # Workflow orchestration
│       ├── services/       # LLM, Spark, and other service abstractions
│       ├── formatters/     # Output formatting utilities
│       ├── models/         # Data models and schemas
│       ├── utils/          # Utility functions
│       ├── prompts/        # LLM prompt templates
│       └── serving/        # MLflow/Databricks serving integration
│
├── notebooks/              # (Optional) Example notebooks
├── tests/                  # Unit and integration tests
├── resources/              # Job and serving configs
├── docs/                   # Project documentation (this folder)
├── setup.py                # Python package setup
├── pyproject.toml          # Build system config
├── requirements.txt        # Python dependencies
├── databricks.yml          # Databricks Asset Bundle config
└── README.md               # Project overview
```

## Flow: How It Works

1. **Agent Orchestration** (`src/eda_agent/agents/eda_agent.py`):
   - Receives a user request (e.g., "analyze this dataset")
   - Uses the LLM Service to interpret intent and select tools/workflows

2. **Workflow Execution** (`src/eda_agent/workflows/`):
   - The agent triggers a workflow (e.g., `basic_eda_workflow.py`)
   - The workflow deterministically calls tools in sequence (e.g., schema detection → summary stats → missing value analysis)

3. **Tool Invocation** (`src/eda_agent/tools/`):
   - Each tool is a modular Python class/function (e.g., `summary_statistics.py`)
   - Tools are registered in a centralized registry (`tool_registry.py`)
   - Tools operate on data via service abstractions (not direct Spark DataFrame manipulation)
   - All outputs are standardized as structured JSON

4. **Service Layer** (`src/eda_agent/services/`):
   - Handles Spark/Delta operations (`spark_service.py`)
   - Handles LLM (ChatDatabricks) calls (`llm_service.py`)
   - Abstracts away Databricks-specific logic for portability

5. **Formatting Layer** (`src/eda_agent/formatters/`):
   - Ensures all tool/workflow outputs are returned in a consistent, machine-readable format (e.g., JSON)

6. **Serving & Deployment**:
   - MLflow integration for model/agent serving (`serving/mlflow_pyfunc.py`)
   - Databricks Asset Bundles for deployment (`databricks.yml`)
   - Jobs and serving configs in `resources/`

7. **Testing & Local Development**:
   - All code is testable locally (VSCode, pytest)
   - Modular design supports rapid iteration and CI/CD

## Intended Use Cases
- Automated, repeatable EDA for data science teams
- Integration with Databricks Model Serving and Jobs
- Enterprise-scale, multi-agent data analysis
- Extensible for new tools, workflows, and LLMs

## Best Practices
- Keep tools modular and stateless
- Use the registry pattern for tool discovery
- Abstract all Spark/Delta/LLM logic into services
- Standardize all outputs for downstream consumption
- Write deterministic workflows for reproducibility
- Use MLflow and Databricks Asset Bundles for deployment

---
For more details, see the README.md and inline code documentation.

