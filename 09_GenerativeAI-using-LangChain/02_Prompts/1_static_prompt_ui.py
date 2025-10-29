from langchain_huggingface import HuggingFaceEndpoint
from langchain_huggingface.chat_models import ChatHuggingFace
from dotenv import load_dotenv
import os
import streamlit as st

load_dotenv()


# Initialize the HuggingFace LLM
llm = HuggingFaceEndpoint(
    repo_id = "openai/gpt-oss-20b",
    task = "text-generation",
    huggingfacehub_api_token=os.getenv("HUGGINGFACE_API_KEY")
) 

model = ChatHuggingFace(llm=llm)

#Streamlit UI 
st.header("Reasearch Tool")

# Static prompt from user instruction
user_input = st.text_input("Enter your question here:")

if st.button("Submit"):
    if user_input.strip() == "":
        st.error("Please enter a question.")
    else:
        st.write("Processing your request...")
        # Invoke the model with user input
        result = model.invoke(user_input)
        st.write("Response:", result)