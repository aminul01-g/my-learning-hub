from langchain_OpenAI import OpenAIEmbeddings
from docenv import load_dotenv
import os

load_dotenv()

embeddings = OpenAIEmbeddings(model="text-embedding-3-large",
                              openai_api_key=os.getenv("OPENAI_API_KEY",
                                                       dimensions=1536))

# Multiple embeddings vectors
document = ["The capital of Bangladesh is Dhaka.",
            "The capital of India is New Delhi.",
            "The capital of Pakistan is Islamabad."
            ]
# Multiple embeddings vectors
Mresult = embeddings.embed_documents(document)
print(str(Mresult))

# Single embedding vector
Sresult = embeddings.embed_query("The capital of Bangladesh is Dhaka.")

print(str(Sresult))