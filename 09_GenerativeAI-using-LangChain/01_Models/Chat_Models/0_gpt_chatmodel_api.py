from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()

model = ChatOpenAI(model ='gpt-4', temperature=1.5)

result = model.invoke("What is the capital of Bangladesh?")

print(result.content)