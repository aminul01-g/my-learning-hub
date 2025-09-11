import pickle
import pandas as pd
import os
from fastapi import HTTPException
from schema.user_input import UserInput as userInput


# Get the absolute path to the model file
MODEL_PATH = os.path.join(os.path.dirname(__file__), "model.pkl")

try:
    # Load pipeline (preprocessing + model together)
    with open(MODEL_PATH, "rb") as f:
        model = pickle.load(f)
except Exception as e:
    print(f"Error loading model: {str(e)}")
    model = None
    
# MLFlow
MODEL_VERSION = '1.0.0'


def predict_insurance_cost(user_input: userInput):
    try:
        if model is None:
            raise HTTPException(status_code=500, detail="Model not loaded. Please check server logs.")
            
        # Convert to DataFrame
        input_data = pd.DataFrame([user_input])
        
        # Ensure all required columns are present
        required_columns = ['age', 'sex', 'bmi', 'children', 'smoker', 'region']
        missing_columns = [col for col in required_columns if col not in input_data.columns]
        if missing_columns:
            raise HTTPException(
                status_code=400, 
                detail=f"Missing required columns: {missing_columns}"
            )

        # Predict using full pipeline
        try:
            prediction = model.predict(input_data)[0]
            prediction = float(max(0, prediction))  # Ensure non-negative prediction
        except Exception as e:
            raise HTTPException(
                status_code=500,
                detail=f"Prediction error: {str(e)}"
            )

        return {
            "predicted_insurance_cost": prediction
        }
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Unexpected error: {str(e)}")
