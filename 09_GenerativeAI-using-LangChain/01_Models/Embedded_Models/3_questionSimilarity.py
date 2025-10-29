from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import os  


load_dotenv()
embeddings = HuggingFaceEmbeddings(model_name = "sentence-transformers/all-MiniLM-L6-v2")

questions = [
    "What is the capital of Bangladesh?",
    "What is the capital of India?",
    "What is the capital of Pakistan?",
    "What is the capital of Sri Lanka?",
    "What is the capital of Nepal?"
]


query = "Tell me about the capital of Bangladesh."

q_embeddings = embeddings.embed_documents(questions)
query_embedding = embeddings.embed_query(query)

similarities = cosine_similarity([query_embedding], q_embeddings)
most_similar_idx = np.argmax(similarities)
most_similar_question = questions[most_similar_idx]

print(f"Most similar question: {most_similar_question}"
      f"\nSimilarity Score: {similarities[0][most_similar_idx]}"
      f"\nIndex: {most_similar_idx}"
      f"\nVector: {q_embeddings[most_similar_idx]}")

