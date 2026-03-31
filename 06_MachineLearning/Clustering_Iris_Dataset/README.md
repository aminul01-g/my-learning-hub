# 🌸 Iris Dataset Clustering (Unsupervised ML)

This project demonstrates the application of three popular unsupervised machine learning algorithms — **K-Means**, **Hierarchical Clustering**, and **DBSCAN** — on the classic **Iris dataset**.  
It also includes **Exploratory Data Analysis (EDA)**, visualization techniques, and clustering performance evaluation.


---

## 📊 Dataset
- **Dataset**: Iris flower dataset
- **Features**: `sepal_length`, `sepal_width`, `petal_length`, `petal_width`
- **Target (unused for clustering)**: `species`

---

## 🔧 Technologies & Libraries
- `Python`
- `pandas`
- `numpy`
- `scikit-learn`
- `matplotlib`
- `seaborn`
- `scipy`

---

## 🛠️ Project Workflow

### 1️⃣ Data Preprocessing
- Loaded dataset from `sklearn`
- Checked for missing values
- Standardized features with `StandardScaler`

### 2️⃣ Exploratory Data Analysis (EDA)
- Pairplot for feature relationships
- Correlation heatmap

### 3️⃣ Clustering Algorithms
- **K-Means**: Elbow method to select `k`
- **Hierarchical Clustering**: Dendrogram analysis
- **DBSCAN**: k-distance plot to estimate `eps`

### 4️⃣ Visualization
- 2D scatter plots
- PCA for dimensionality reduction
- Dendrogram for Hierarchical Clustering
- DBSCAN clusters with noise points identified

### 5️⃣ Evaluation (Optional but included)
- Confusion Matrix (True Labels vs. Cluster Labels)
- Adjusted Rand Index (Clustering Quality)

---

## 📈 Results Summary
| Algorithm    | Performance           | Visualization Insight    |
|--------------|-----------------------|---------------------------|
| **K-Means**  | Strong, clean clusters | Matches expected species   |
| **Hierarchical** | Similar to K-Means | Clear cluster separation    |
| **DBSCAN**   | Sensitive to `eps`     | Identifies noise points     |

---

## 🚀 How to Run
1. Clone this repository  
```bash
git clone https://github.com/<your-username>/Clustering_Iris_Dataset.git
cd iris-clustering
```

2. Install dependencies
```bash
pip install -r requirements.txt

```

### 📌 Key Learnings

✅ How to perform unsupervised clustering
✅ How to interpret dendrograms & density-based clustering
✅ When to use PCA for visualization
✅ How to evaluate clustering with Adjusted Rand Index

📄 License

This project is open-source and available under the MIT License.

### 🤝 Acknowledgements

 - Dataset: Iris Dataset - sklearn
 - Inspired by standard ML clustering workflows.

### ✨ Contact

If you'd like to connect, discuss, or collaborate, feel free to reach out!
