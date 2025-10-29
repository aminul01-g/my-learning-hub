from langchain.prompts import ChatPromptTemplate
from langchain.schema import HumanMessage, AIMessage  # <-- import message types
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

# Initialize the chat model
model = ChatHuggingFace(llm=llm)

# Define a prompt template
chat_template = ChatPromptTemplate([
    ("system", "You are a helpful {domain} expert."),
    ("human", "{user_input}"),
])

# Format the prompt with actual values
prompt = chat_template.invoke({
    "domain": "AI",
    "user_input": "What is LangChain?"
})

print(prompt)