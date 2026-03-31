# 🔮 LSTM-based Next Word Prediction in PyTorch

This project implements a word-level LSTM model using PyTorch to predict the next word based on input text. It demonstrates preprocessing, vocabulary building, training, and inference on a real-world dataset (FAQ document).

## 📚 Project Overview

This LSTM model learns to predict the next word in a sentence. It covers:
- Tokenization and vocabulary creation using NLTK
- Training data preparation with padding
- Custom Dataset and DataLoader
- LSTM model with embedding and linear layers
- Training loop and evaluation
- Prediction and accuracy computation

## 🧠 Model Architecture

- `nn.Embedding`: Converts word indices to dense vectors
- `nn.LSTM`: Learns word sequence patterns
- `nn.Linear`: Predicts the next word

## 🚀 Getting Started

### Install Dependencies
```bash
pip install torch nltk
```

## 📊 Output
- Training loss per epoch
- Final model accuracy
- Sample word predictions

## 📌 File Structure
- `lstm.ipynb`: Full implementation of preprocessing, model training, and prediction

## 📝 License
Open-source and free to use for educational purposes.
