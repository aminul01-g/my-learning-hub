from langchain_community.document_loaders import WebBaseLoader
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
    input_variables=["question","text"],
    template="Answer the following question:\n{question} from the following text - \n{text}"
)

parser = StrOutputParser()



loader = WebBaseLoader("https://en.wikipedia.org/wiki/Artificial_intelligence")

documents = loader.load()

print(f"Number of documents: {len(documents)}")
print(documents[0].page_content)
print(documents[0].metadata)


chain = prompt | model | parser


print(chain.invoke({'question': 'what is AI?', 'text':documents[0].page_content}))