from langchain_huggingface import HuggingFaceEndpoint
from langchain_huggingface.chat_models import ChatHuggingFace
from dotenv import load_dotenv
import os

from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableParallel

load_dotenv()

# Initialize HuggingFace LLM
llm1 = HuggingFaceEndpoint(
    repo_id="openai/gpt-oss-20b",
    task="text-generation",
    huggingfacehub_api_token=os.getenv("HUGGINGFACE_API_KEY")
)

# Define the model
llm2 = HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",
    task="text-generation",
    huggingfacehub_api_token=os.getenv("HUGGINGFACE_API_KEY")
)


model1 = ChatHuggingFace(llm = llm1)

model2 = ChatHuggingFace(llm = llm2)

prompt1 = PromptTemplate(
    input_variables=["topic"],
    template="Generate short and simple note from the following {topic}?",
)

prompt2 = PromptTemplate(
    input_variables=["topic"],
    template="Generate 5 short questions answers from the following {topic}?",
)

prompt3 = PromptTemplate(
    input_variables=["notes", "qna"],
    template="Combine the following notes: {notes} and QnA: {qna} into a single comprehensive summary.",
)

parser=StrOutputParser()

Parallel_chain = RunnableParallel(
    {
        "notes": prompt1 | model1 | parser,
        "qna": prompt2 | model2 | parser,
    }
) 

marge_chain = prompt3 | model1 | parser  

chain = Parallel_chain | marge_chain

response = chain.invoke({"topic": "The impact of climate change on global agriculture"})
print(response)

chain.get_graph().print_ascii()