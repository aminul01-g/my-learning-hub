from langchain_text_splitters import CharacterTextSplitter

text = """LangChain is a framework for developing applications powered by language models. It can be used for chatbots, Generative Question-Answering (GQA), summarization, and much more.
The core idea of the library is that we can "chain" together different components to create more advanced use cases around LLMs.
Chains may consist of multiple components from prompt templates to LLMs to other utilities. Chains can be simple, with just a single prompt and LLM, or more complex with multiple components.
Chains can also be serialized to JSON and re-loaded. This makes it easy to share and reproduce chains."""

splitter = CharacterTextSplitter(
    separator="",
    chunk_size=100,
    chunk_overlap=20,
    length_function=len,
)

split_texts = splitter.split_text(text)

print(split_texts)
