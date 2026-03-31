# Simple Question Answering Model

[![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white)](https://pytorch.org/)
[![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)

This project presents a foundational Question Answering (QA) model built with a Simple Recurrent Neural Network (RNN) in PyTorch. The model is trained on a curated dataset of 100 unique question-answer pairs to illustrate the fundamental concepts of sequence-to-sequence modeling for QA tasks.

## Project Overview

The goal of this project is to demonstrate a basic implementation of an RNN-based QA system. It covers essential steps from data preparation to model training and inference.

## Features

- **Data Preprocessing:** Includes tokenization and vocabulary creation from the dataset.
- **RNN Model:** A simple RNN architecture designed for sequence processing.
- **Training Loop:** Implements a standard training procedure with loss calculation and optimizer updates.
- **Prediction Function:** Allows for generating answers to new questions based on the trained model.

## Dataset

The model is trained on a dataset containing 100 unique question-answer pairs. This dataset is included with the project for reproducibility.

## Model Architecture

The `SimpleRNN` model comprises the following layers:

- **`nn.Embedding`:** Maps input tokens to dense vector representations.
- **`nn.RNN`:** Processes the sequence of embedded tokens to capture temporal dependencies.
- **`nn.Linear`:** Transforms the RNN's output to the size of the vocabulary for predicting the next token.

## Getting Started

### Prerequisites

Ensure you have the following installed:

- Python 3.x
- PyTorch (`torch`)
- Pandas (`pandas`)
