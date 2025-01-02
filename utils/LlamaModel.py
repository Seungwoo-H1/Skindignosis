# LlamaModel.py
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import AssistantMessage, SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential

# LlamaModel 클래스
class LlamaModel:
    def __init__(self, endpoint, api_key, model_name):
        self.client = ChatCompletionsClient(
            endpoint=endpoint,
            credential=AzureKeyCredential(api_key)
        )
        self.model_name = model_name

    def generate_feedback_text(self, prompt):
        messages = [
            SystemMessage(content="You are a helpful assistant."),
            UserMessage(content=prompt)
        ]

        try:
            response = self.client.complete(messages=messages, model=self.model_name)
            assistant_message = response.choices[0].message.content
            return assistant_message
        except Exception as e:
            return f"Failed to call the model. Error: {e}"


