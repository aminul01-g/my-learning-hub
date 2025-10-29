from langchain_huggingface import HuggingFaceEndpoint
from langchain_huggingface.chat_models import ChatHuggingFace
from dotenv import load_dotenv
import os
from langchain.schema import HumanMessage, AIMessage  # <-- import message types

load_dotenv()

# Initialize HuggingFace LLM
llm = HuggingFaceEndpoint(
    repo_id="openai/gpt-oss-20b",
    task="text-generation",
    huggingfacehub_api_token=os.getenv("HUGGINGFACE_API_KEY")
)

model = ChatHuggingFace(llm=llm)

chat_history = []  # will store HumanMessage / AIMessage objects

while True:
    input_text = input("You: ")
    
    # Add user message
    chat_history.append(HumanMessage(content=input_text))
    
    if input_text.lower() in ['exit', 'quit']:
        print("Exiting the chatbot. Goodbye!")
        break

    # Call the model with list of BaseMessages
    response = model.invoke(chat_history)

    # Add assistant reply
    chat_history.append(AIMessage(content=response.content))

    print("Bot:", response.content)

print("messages:", chat_history)
