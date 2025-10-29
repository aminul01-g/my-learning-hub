from langchain_huggingface import HuggingFaceEndpoint
from langchain_huggingface.chat_models import ChatHuggingFace
from dotenv import load_dotenv
import os

from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableBranch, RunnableLambda
from langchain_community.document_loaders import TextLoader

load_dotenv()

# Initialize HuggingFace LLM
llm1 = HuggingFaceEndpoint(
    repo_id="openai/gpt-oss-20b",
    task="text-generation",
    huggingfacehub_api_token=os.getenv("HUGGINGFACE_API_KEY")
)

model = ChatHuggingFace(llm=llm1)

prompt = PromptTemplate(
    input_variables=["text"],
    template="Write a summary for the following text:\n\n{text}"
)

parser = StrOutputParser()

# Load your text file
loader = TextLoader("text.txt", encoding="utf-8")
documents = loader.load()

print(type(documents))
print(len(documents))
print(documents[0].page_content)
print(documents[0].metadata)


# Correct chain order: prompt → model → parser
chain = prompt | model | parser

# Invoke correctly using variable name that matches the prompt
result = chain.invoke({"text": documents[0].page_content})

print(result)
