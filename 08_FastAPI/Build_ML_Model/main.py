from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse

from model.predict import predict_insurance_cost as make_prediction, MODEL_VERSION, model
from schema.user_input import UserInput as userInput

app = FastAPI(
    title="Insurance Cost Prediction API",
    description="API for predicting insurance costs based on personal information",
    version="1.0.0"
)



# Human readable root endpoint
@app.get("/")
def home():
    return {
        "message": "Welcome to the Insurance Cost Prediction API.",
        "endpoints": {
            "/predict": "POST endpoint for getting insurance cost predictions",
            "/health": "GET endpoint for checking API health"
        }
    }

# Server health check endpoint
@app.get("/health")
def health_check():
    if model is None:
        raise HTTPException(
            status_code=503,
            detail="Model is not loaded. Service is unavailable."
        )
    return {
        "status": "healthy",
        "model_version": MODEL_VERSION,
        "model_loaded": True
    }

@app.post("/predict")
def predict_insurance_cost_route(user_input: userInput):
    try:
        prediction = make_prediction(user_input)
        if isinstance(prediction, dict):
            prediction["predicted_insurance_cost"] = round(float(prediction["predicted_insurance_cost"]), 2)
            return JSONResponse(content=prediction)
        return JSONResponse(content={"predicted_insurance_cost": round(float(prediction), 2)})
    except HTTPException as he:
        raise he
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# To run the app, use the command:
# uvicorn main:app --reload
# Generate the requirements file using:
# pip freeze > requirements.txt