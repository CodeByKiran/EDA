import mlflow.pyfunc
from ..workflows.basic_eda_workflow import BasicEDAWorkflow

class EDAAgentPyFuncModel(mlflow.pyfunc.PythonModel):
    def load_context(self, context):
        self.data_path = context.artifacts.get("data_path", None)

    def predict(self, context, model_input):
        workflow = BasicEDAWorkflow(self.data_path)
        return workflow.run()

