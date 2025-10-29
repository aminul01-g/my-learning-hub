# LLM with HuggingFacePipeline

from langchain_huggingface import HuggingFacePipeline

# Load a text-generation model (LLM)
llm = HuggingFacePipeline.from_model_id(
    model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",  # small, free, fast model
    task="text-generation",
    pipeline_kwargs=dict(
        temperature=0.7,
        max_new_tokens=200,
    )
)

# Use it directly (no Chat wrapper)
result = llm.invoke("Explain quantum computing in simple terms.")
print(result)
