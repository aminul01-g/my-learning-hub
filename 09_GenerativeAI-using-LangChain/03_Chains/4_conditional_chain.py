from langchain_huggingface import HuggingFaceEndpoint
from langchain_huggingface.chat_models import ChatHuggingFace
from dotenv import load_dotenv
import os

from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser, PydanticOutputParser
from langchain.schema.runnable import RunnableBranch, RunnableLambda
from pydantic import BaseModel, Field
from typing import Literal

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


parser1 = StrOutputParser()

class FeedbackSchema(BaseModel):
    sentiment: Literal["positive", "negative"] = Field(..., description="The sentiment of the feedback")

parser2 = PydanticOutputParser(pydantic_object=FeedbackSchema)

prompt1 = PromptTemplate(
    input_variables=["feedback"],
    partial_variables={"format_instruction": parser2.get_format_instructions()},
    template="Classify the sentiment of the following text into postive or negative\n {feedback} \n {format_instruction}?",
)

classifer_chain = prompt1 | model1 | parser2

prompt2 = PromptTemplate(
    input_variables=["feedback"],
    template="Generate an Actionable response to this positive feedback:\n {feedback}?",
)

prompt3 = PromptTemplate(
    input_variables=["feedback"],
    template="Generate an Actionable response to this negative feedback:\n {feedback}?",
)

branch_chain = RunnableBranch(
    (lambda x: x.sentiment == 'positive', prompt2 | model1 | parser1),
    (lambda x: x.sentiment == 'negative', prompt3 | model2 | parser1),
    RunnableLambda(lambda x: "No valid sentiment found.")
)



chain = classifer_chain | branch_chain

response = chain.invoke({"feedback": "The product quality is excellent and I am very satisfied with my purchase!"})
print(response)

chain.get_graph().print_ascii()