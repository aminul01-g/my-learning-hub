from langchain_community.document_loaders import PyPDFLoader


loader = PyPDFLoader("CSE_342_Lab_Report.pdf")

pages = loader.load()

print(pages[0].page_content)

print(f"Number of pages: {len(pages)}")