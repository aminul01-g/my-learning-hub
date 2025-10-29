from langchain_huggingface import HuggingFaceEndpoint
from langchain_huggingface.chat_models import ChatHuggingFace
from dotenv import load_dotenv
import os
import streamlit as st
from langchain.prompts import PromptTemplate


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

# Dynamic prompt from user instruction
paper_input = st.selectbox("Select a research paper topic:", 
                          ["Artificial Intelligence", "Climate Change", "Quantum Computing", "Renewable Energy", "Blockchain Technology"])
style_input = st.selectbox("Select response style:", 
                          ["Formal", "Casual", "Technical", "Humorous", "Inspirational"])
length_input = st.selectbox("Select response length:", 
                          ["Short (1-2 sentences)", "Medium (1-2 paragraphs)", "Long (3-4 paragraphs)"])

# Create a dynamic prompt template
template = ("Here is a summary of a research paper on {paper_topic} "
            "in a {response_style} style with {response_length} length.")
prompt = PromptTemplate.from_template(template)
user_input = prompt.format(paper_topic=paper_input, response_style=style_input, response_length=length_input)



if st.button("Submit"):
    st.write ("Here is a summary of a research paper on", paper_input, "in a", style_input, "style with", length_input, "length.")
    if user_input.strip() == "":
        st.error("Please enter a question.")
    else:
        st.write("Processing your request...")
        # Invoke the model with user input
        result = model.invoke(user_input)
        st.write("Response:", result)