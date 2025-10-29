from langchain_community.document_loaders import DirectoryLoader

loader = DirectoryLoader("data/", glob="**/*.txt")

documents = loader.load()

print(f"Number of documents: {len(documents)}")
print(documents[0].page_content)