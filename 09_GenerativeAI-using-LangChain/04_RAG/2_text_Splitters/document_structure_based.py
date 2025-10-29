from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader("CSE_342_Lab_Report.pdf")

pages = loader.load()

splitter = CharacterTextSplitter(
    separator="",
    chunk_size=200,
    chunk_overlap=0,
    length_function=len,
)

result = splitter.split_documents(pages)

print(result[0].page_content)