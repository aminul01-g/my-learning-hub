from langchain_community.document_loaders import CSVLoader

loader = CSVLoader(file_path ='')

# for every row of data you got docs obj

docs = loader.load()

print(len(docs))