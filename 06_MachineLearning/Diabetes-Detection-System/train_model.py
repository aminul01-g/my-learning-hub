# train_model.py

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import pickle

# Load dataset (use the same file you used for your project)
data = pd.read_csv("diabetes.csv")  # Make sure this file exists in the same folder

# Split into features and target
X = data.drop("Outcome", axis=1)
y = data["Outcome"]

# Train-test split (optional here, just for training the model)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Random Forest model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Save the trained model
with open("trained_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("✅ Model trained and saved as trained_model.pkl")
