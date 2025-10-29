from langchain_huggingface import HuggingFaceEndpoint
from langchain_huggingface.chat_models import ChatHuggingFace
from dotenv import load_dotenv
import os
import streamlit as st
from langchain.prompts import PromptTemplate,load_prompt

load_dotenv()

# Initialize the HuggingFace LLM
llm = HuggingFaceEndpoint(
    repo_id = "openai/gpt-oss-20b",
    task = "text-generation",
    huggingfacehub_api_token=os.getenv("HUGGINGFACE_API_KEY")
) 

model = ChatHuggingFace(llm=llm)

#Streamlit UI 
st.header('Reasearch Tool')

# Dynamic prompt from user instruction
paper_input = st.selectbox( "Select Research Paper Name", ["Attention Is All You Need", "BERT: Pre-training of Deep Bidirectional Transformers", "GPT-3: Language Models are Few-Shot Learners", "Diffusion Models Beat GANs on Image Synthesis"] )

style_input = st.selectbox( "Select Explanation Style", ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"] ) 

length_input = st.selectbox( "Select Explanation Length", ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"] )

template = load_prompt('template.json')



if st.button('Summarize'):
    # Create a chain with the prompt template and model
    chain = template | model
    result = chain.invoke({
        'paper_input':paper_input,
        'style_input':style_input,
        'length_input':length_input
    })
    st.write(result.content)