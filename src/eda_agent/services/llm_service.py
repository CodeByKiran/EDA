from langchain.chat_models import ChatDatabricks

class LLMService:
    """Centralized LLM service for ChatDatabricks."""
    def __init__(self, endpoint: str = None):
        self.llm = ChatDatabricks(endpoint=endpoint)

    def chat(self, messages):
        return self.llm(messages)

