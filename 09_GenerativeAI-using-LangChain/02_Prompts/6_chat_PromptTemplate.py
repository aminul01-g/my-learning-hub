from langchain.prompts import ChatPromptTemplate
from langchain.schema import HumanMessage, AIMessage
from langchain_huggingface import HuggingFaceEndpoint
from langchain_huggingface.chat_models import ChatHuggingFace
from dotenv import load_dotenv
import os

load_dotenv()

# Initialize HuggingFace LLM
llm = HuggingFaceEndpoint(
    repo_id="openai/gpt-oss-20b",
    task="text-generation",
    huggingfacehub_api_token=os.getenv("HUGGINGFACE_API_KEY")
)

# Initialize chat model
model = ChatHuggingFace(llm=llm)

# Define prompt template
chat_template = ChatPromptTemplate([
    ("system", "You are a helpful {domain} expert."),
    ("human", "{user_input}"),
])

chat_history = []

while True:
    input_text = input("You: ")

    # Add user message
    chat_history.append(HumanMessage(content=input_text))
    
    if input_text.lower() in ['exit', 'quit']:
        print("Exiting the chatbot. Goodbye!")
        break

    # Format the prompt with user input
    prompt = chat_template.invoke({
        "domain": "AI",
        "user_input": input_text
    })

    # Send to model
    response = model.invoke(prompt)

    # Add messages to history

    chat_history.append(AIMessage(content=response.content))

    print("Bot:", response.content)

print("Chat ended. Full history:\n\n", chat_history)
print(prompt)
