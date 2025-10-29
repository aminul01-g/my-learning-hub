
from langchain_huggingface import HuggingFaceEndpoint
from langchain_huggingface.chat_models import ChatHuggingFace
from dotenv import load_dotenv
import os

from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

# Initialize HuggingFace LLM
llm = HuggingFaceEndpoint(
    repo_id="openai/gpt-oss-20b",
    task="text-generation",
    huggingfacehub_api_token=os.getenv("HUGGINGFACE_API_KEY")
)

prompt = PromptTemplate(
    input_variables=["product"],
    template="What is a good name for 2 companys that makes {product}?",
)

model = ChatHuggingFace(llm=llm)

parser = StrOutputParser()

chian = prompt | model | parser

result = chian.invoke({"product": "colorful socks"})

print(result)

chian.get_graph().print_ascii()