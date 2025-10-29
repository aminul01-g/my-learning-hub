from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv
import os  

load_dotenv()
embeddings = HuggingFaceEmbeddings(model_name = "sentence-transformers/all-MiniLM-L6-v2")


# Multiple embeddings vectors
document = ["The capital of Bangladesh is Dhaka.",
            "The capital of India is New Delhi.",
            "The capital of Pakistan is Islamabad."
            ]
# Multiple embeddings vectors
Mresult = embeddings.embed_documents(document)
print(str(Mresult))

# single embedding vector
text = "The capital of Bangladesh is Dhaka."
vector = embeddings.embed_query(text)

print(str(vector))