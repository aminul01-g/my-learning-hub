# 🎯 Fine-Tuning Open-Source Models

This directory focuses on the practical aspects of fine-tuning Large Language Models (LLMs) using modern, parameter-efficient techniques.

## 🏗️ Folder Structure

- **[`CausalLM`](./CausalLM)**: Notebooks for fine-tuning Decoder-only models (e.g., Qwen, Llama, Gemma).
- **[`Encoder`](./Encoder)**: Fine-tuning Encoder-only models for classification and embedding tasks (e.g., BERT, RoBERTa).
- **[`Seq2Seq`](./Seq2Seq)**: Fine-tuning Encoder-Decoder models for translation and summarization (e.g., T5, BART).

## 🚀 Key Techniques Covered

- **LoRA (Low-Rank Adaptation)**: Efficiently updating a small subset of parameters.
- **QLoRA**: 4-bit quantization for fine-tuning on consumer GPUs (like the NVIDIA T4).
- **Unsloth**: Optimized training kernels for faster and more memory-efficient fine-tuning.
- **SFT (Supervised Fine-Tuning)**: Instruction-tuning models on specific datasets.

## 🛠️ Requirements & Setup

To run these notebooks, it is recommended to use an environment with:
- `transformers`
- `peft`
- `trl`
- `bitsandbytes`
- `accelerate`
- `unsloth` (for optimized fine-tuning)

### Installation
```bash
pip install -U "unsloth[colab-new] @ git+https://github.com/unslothai/unsloth.git"
pip install --no-deps "xformers<0.0.27" "trl<0.9.0" peft accelerate bitsandbytes
```

---
*Part of the [AI Engineering Roadmap](../README.md)*
