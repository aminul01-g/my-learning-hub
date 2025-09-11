from fastapi import FastAPI, Path, HTTPException, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field, computed_field
from typing import Annotated
import json

app = FastAPI()

# Define a Pydantic model for Patient data validation
class Patient(BaseModel):
    id: str = Field(..., title="ID of the patient", description="Unique ID of the patient", example="12345")
    name: str = Field(..., title="Name of the patient", description="Full name of the patient", example="John Doe")
    city: str = Field(..., title="City of the patient", description="City where the patient lives", example="New York")
    age: int = Field(..., gt=0, lt=120, title="Age of the patient", description="Age must be between 1 and 119", example=30)
    gender: str = Field(..., title="Gender of the patient", description="Gender of the patient", example="Male/Female")
    height: float = Field(..., gt=0, title="Height of the patient", description="Height in cm", example=175.5)
    weight: float = Field(..., gt=0, title="Weight of the patient", description="Weight in kg", example=70.5)


    #computed fields for BMI and BMI category
    @computed_field
    @property
    def bmi(self) -> float:
        return self.weight / ((self.height / 100) ** 2)


    #computed field for BMI category
    @computed_field
    @property
    def bmi_category(self) -> str:
        bmi_value = self.bmi
        if bmi_value < 18.5:
            return "Underweight"
        elif 18.5 <= bmi_value < 24.9:
            return "Normal weight"
        elif 25 <= bmi_value < 29.9:
            return "Overweight"
        else:
            return "Obesity"

# functions to load data
def load_data():
    with open('patients.json', 'r') as file:
        data = json.load(file)
    return data

# function to save data
def save_data(data):
    with open('patients.json', 'w') as file:
        json.dump(data, file)


# define create endpoint
@app.post("/create")
def create_patient(patient: Patient):
    
    # load existing patients from a database or file (simulated here with a list)
    data = load_data()
    
    # Check if patient with same ID already exists
    if patient.id in data:
        raise HTTPException(status_code=400, detail="Patient with this ID already exists")  
    
    
    # new patient added to the database
    data[patient.id] = patient.model_dump(exclude=['id'])
    
    
    # Save the updated data back to the JSON file
    save_data(data)
    
    return JSONResponse(status_code=201, content={"message": "Patient created successfully"})