
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

prompt1 = PromptTemplate(
    input_variables=["topic"],
    template="Generate a detailed report on {topic}?",
)

prompt2 =  PromptTemplate(
    input_variables=["report"],
    template="Summarize the following report in a concise manner with in 5 points: {report}",
)

model = ChatHuggingFace(llm = llm)

parser=StrOutputParser()

chain = prompt1 | model | parser | prompt2 | model | parser

response = chain.invoke({"topic": "The impact of climate change on global agriculture"})
print(response)

chain.get_graph().print_ascii()