import vertexai
from vertexai.language_models import CodeChatModel

vertexai.init(project="proven-cosine-402618", location="us-central1")
chat_model = CodeChatModel.from_pretrained("codechat-bison-32k")
parameters = {
    "max_output_tokens": 1024,
    "temperature": 0.2
}
chat = chat_model.start_chat()
response = chat.send_message("""Write Fibonacci code in python3""", **parameters)
print(f"Response from Model: {response.text}")
