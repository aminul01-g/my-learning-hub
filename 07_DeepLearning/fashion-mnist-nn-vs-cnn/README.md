# 🧠 Neural Network vs CNN on Fashion MNIST

This project compares a fully connected Neural Network (NN) and a Convolutional Neural Network (CNN) on the Fashion MNIST dataset using PyTorch.

## 📌 Key Features

- Implementation of both NN and CNN using PyTorch
- Visual training history (accuracy and loss)
- Displays 5 sample test predictions with actual vs predicted labels
- Final test accuracy comparison between models
- Clean and reproducible notebook

## 📊 Final Accuracy

| Model | Test Accuracy |
|-------|---------------|
| NN    | 87.21%        |
| CNN   | 91.72%        |

✅ CNN outperformed NN by 4.52%%

## 📁 Structure

```
NN-vs-CNN-FashionMNIST/
├── NN_vs_CNN.ipynb    # Main notebook
├── README.md                     # Project documentation            
└── requirements.txt/             # Python dependencies
```

## 🚀 Getting Started

1. Clone the repository
2. Install dependencies:
```bash
pip install -r requirements.txt
```
3. Download the `fashion-mnist.csv` dataset.
4. Run the notebook.

## 🧰 Tech Stack

- Python
- PyTorch
- Matplotlib
- scikit-learn
