
# LLM with HuggingFaceEndpoint (API hosted)

from langchain_huggingface import HuggingFaceEndpoint
import os
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="tiiuae/falcon-7b-instruct",  # hosted on HF
    task="text-generation",
    huggingfacehub_api_token=os.getenv("HUGGINGFACE_API_KEY")
)

result = llm.invoke("What is the capital of Bangladesh?")
print(result)
