from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
import os

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="openai/gpt-oss-20b",
    task="text-generation",
     huggingfacehub_api_token=os.getenv("HUGGINGFACE_API_KEY") 
)

model = ChatHuggingFace(llm=llm)

result = model.invoke("how you can help me?")

print(result.content)