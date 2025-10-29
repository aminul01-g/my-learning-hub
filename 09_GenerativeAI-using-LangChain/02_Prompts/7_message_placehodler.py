
from langchain_huggingface import HuggingFaceEndpoint
from langchain_huggingface.chat_models import ChatHuggingFace
from dotenv import load_dotenv
import os

from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.schema import HumanMessage, AIMessage


load_dotenv()

# Initialize HuggingFace LLM
llm = HuggingFaceEndpoint(
    repo_id="openai/gpt-oss-20b",
    task="text-generation",
    huggingfacehub_api_token=os.getenv("HUGGINGFACE_API_KEY")
)

# Wrap in chat model
model = ChatHuggingFace(llm=llm)

# Define prompt template with history
chat_template = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful {domain} expert."),
    MessagesPlaceholder(variable_name="history"),
    ("human", "{user_input}"),
])

chat_history = []  # will store HumanMessage / AIMessage

# Load chat history if file exists
if os.path.exists("chat_history.txt"):
    with open("chat_history.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            if line.startswith("User:"):
                content = line.replace("User:", "").strip()
                chat_history.append(HumanMessage(content=content))
            elif line.startswith("Bot:"):
                content = line.replace("Bot:", "").strip()
                chat_history.append(AIMessage(content=content))

while True:
    input_text = input("You: ")

    # Add user message
    chat_history.append(HumanMessage(content=input_text))


    if input_text.lower() in ['exit', 'quit']:
        print("Exiting the chatbot. Goodbye!")
        # Save history before quitting
        with open("chat_history.txt", "a") as file:
            for msg in chat_history:
                if isinstance(msg, HumanMessage):
                    file.write(f"User: {msg.content}\n")
                elif isinstance(msg, AIMessage):
                    file.write(f"Bot: {msg.content}\n")
        break

    # Build final prompt with history
    prompt = chat_template.invoke({
        "domain": "AI",
        "history": chat_history,
        "user_input": input_text
    })

    # Generate response
    response = model.invoke(prompt)

    # Add assistant reply
    chat_history.append(AIMessage(content=response.content))

    print("Bot:", response.content)
    
print("Chat ended. Full history:\n\n", chat_history)
print(prompt)