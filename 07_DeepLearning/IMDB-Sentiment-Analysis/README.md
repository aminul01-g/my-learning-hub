# IMDB Sentiment Analysis (Research-Focused)

## Abstract
This project investigates sentiment classification on the **IMDB Movie Reviews dataset**, a widely used benchmark for natural language processing (NLP) tasks. The primary objective is to build and evaluate machine learning models that classify reviews as **positive** or **negative**, and to analyze their effectiveness using both traditional and modern approaches.

---

## 📂 Dataset
- **Source**: [IMDB Dataset of 50K Movie Reviews](https://ai.stanford.edu/~amaas/data/sentiment/)  
- **Size**: 50,000 reviews (25K for training, 25K for testing)  
- **Labels**:  
  - `0` → Negative sentiment  
  - `1` → Positive sentiment  

Preprocessing steps include:
- Tokenization  
- Lowercasing  
- Stopword removal  
- Lemmatization  
- Vectorization using **TF-IDF**  

---

## Methodology
We experimented with both **traditional machine learning** and **deep learning** methods:

1. **Baseline Models**
   - Logistic Regression  
   - Naïve Bayes  
   - Support Vector Machines (SVM)  

2. **Deep Learning Models**
   - Artificial Neural Networks (ANN)  
   - Recurrent Neural Networks (RNN, LSTM)  

3. **Feature Engineering**
   - Bag-of-Words  
   - TF-IDF  
   - Word Embeddings (Word2Vec, GloVe, BERT)  

4. **Evaluation Metrics**
   - Accuracy  
   - Precision, Recall, F1-Score  

---

## 📊 Results

### Model Performance Comparison

| Method                  | Accuracy | Precision | Recall | F1-Score |
|-------------------------|----------|-----------|--------|----------|
| BERT (CLS) + LR (Test) | 81%     | 0.82      | 0.80   | 0.81     |
| BERT (CLS) + LR (Val)           | 81%     | 0.82      | 0.80   | 0.81     |
| TF–IDF + LR (Test)  | 88%     | 0.88      | 0.89   | 0.89     |
| TF–IDF + LR (Val)  | 89%     | 0.88      | 0.90   | 0.89     |
| Word2Vec + LR (Test)   | 85%     | 0.85      | 0.84   | 0.85     |
| Word2Vec + LR (Val)   | 86%     | 0.86      | 0.87   | 0.86     |


---

## 🌎 Discussion & Future Work
- **Strengths**:  
  - Simple preprocessing with TF-IDF yields strong baseline results.  
  - Deep learning models capture context and semantics better, improving F1-score.  

- **Limitations**:  
  - LSTM and BERT training are computationally expensive.  
  - Generalization to other domains (e.g., product reviews) is untested.  

- **Future Work**:  
  - Fine-tune transformer-based models (BERT, RoBERTa) for higher accuracy.  
  - Apply domain adaptation for other review datasets.  
  - Incorporate explainability tools (LIME, SHAP) to interpret predictions.  

---


## 📍 References
- Maas, A. L., et al. (2011). *Learning Word Vectors for Sentiment Analysis*. ACL.  
- Pedregosa, F., et al. (2011). *Scikit-learn: Machine Learning in Python*. JMLR.  
- Mikolov, T., et al. (2013). *Efficient Estimation of Word Representations in Vector Space*.  

---

## 👌 Acknowledgments
This project was developed as part of **IMDB Sentiment Analysis** in the AI/ML learning journey. Special thanks to the open-source community for providing tools and datasets that enabled this research.

