# 🏡 Predictive Modeling of Ames Housing Data (Simulated Version)

This project demonstrates a full machine learning pipeline for predicting house prices using a simulated version of the **Ames Housing dataset**. The workflow includes data simulation, preprocessing, feature engineering, model training, evaluation, and interpretation — all within a single Jupyter notebook.

---

## 📌 Overview

The goal is to build and compare different regression models to predict the log-transformed house prices (`SalePrice`) based on important structural and neighborhood features.

Key steps covered:
- Simulating an Ames-like dataset
- Data cleaning and feature transformation
- Pipeline creation using Scikit-Learn
- Model comparison (Linear Regression, Ridge, Lasso)
- Interpretation of Ridge Regression coefficients

---

## 📁 Repository Contents

📦 Predictive-Modeling-of-Ames-Housing-Data
      ├── Ames_Housing_Modeling_Fixed.ipynb # Main Jupyter notebook
      ├── README.md # Project description and instructions
      └── requirements.txt # Python dependencies (optional)


---

## 📈 Dataset Description

The dataset used here is a **simulated subset** of the Ames Housing dataset. It mimics real-world property data with fields such as:

- `OverallQual`: Overall material and finish quality
- `GrLivArea`: Above grade (ground) living area square feet
- `GarageCars`: Size of garage in car capacity
- `LotFrontage`: Linear feet of street connected to property
- `Neighborhood`: Physical locations within Ames city
- `SalePrice`: Log-transformed sale price of the house (target)

---

## 🧪 Models Used

- **Linear Regression**
- **Ridge Regression** (α = 10)
- **Lasso Regression** (α = 0.01)

Model performance is evaluated using:
- **Cross-validated R² Score**
- **Root Mean Squared Error (RMSE)**

---

## 🧠 Key Findings

- **Ridge Regression** demonstrated the most robust and consistent performance across folds.
- Important predictors include `Neighborhood`, `HouseAge`, and `GrLivArea`.
- The notebook includes coefficient interpretation to explain model decisions.

---

## 🚀 How to Run

### 1. Clone the repository

```bash
git clone https://github.com/aminul01-g/Predictive-Modeling-of-Ames-Housing-Data.git
cd Predictive-Modeling-of-Ames-Housing-Data
```

### 2. Launch Jupyter Notebook
If Jupyter is installed:

```bash
jupyter notebook Ames_Housing_Modeling_Fixed.ipynb
```
Or open it in Google Colab (recommended for beginners).

### 📦 Requirements
Install the necessary packages using:
```bash
pip install -r requirements.txt
```
Or manually ensure the following are installed:

Python 3.8+

pandas

numpy

scikit-learn

matplotlib (optional for visualizations)

### 📚 References
[Original Ames Housing Dataset](https://jse.amstat.org/v19n3/decock.pdf)

[Scikit-Learn Documentation](https://scikit-learn.org/stable/user_guide.html)

### 📄 License
This project is licensed under the MIT License.

### 🙋‍♂️ Author
Developed by Aminul — feel free to connect or suggest improvements!


---
