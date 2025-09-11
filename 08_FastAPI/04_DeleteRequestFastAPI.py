from fastapi import FastAPI, Path, HTTPException, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field, computed_field
from typing import Annotated, Optional
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



# Define a Pydantic model for updating Patient data
class PatientUpdate(BaseModel):
    name : Annotated[Optional[str], Field(default = None)]
    city : Annotated[Optional[str], Field(default = None)]
    age : Annotated[Optional[int], Field(default = None, gt=0)]
    gender : Annotated[Optional[str], Field(default = None)]
    height : Annotated[Optional[float], Field(default = None, gt=0)]
    weight : Annotated[Optional[float], Field(default = None, gt=0)]




# functions to load data
def load_data():
    with open('patients.json', 'r') as file:
        data = json.load(file)
    return data

# function to save data
def save_data(data):
    with open('patients.json', 'w') as file:
        json.dump(data, file)







# define a root endpoint
@app.get("/")
def hello():
    return {"message": "Welcome to the Patient Management API. Use /docs for interactive API documentation."}








# define an endpoint for Path parameters
@app.get("/patient/{patient_id}")
def view_patient(patient_id: str = Path(..., description = "Id of the patient in DB",
                                         example = "P001")):
    # load data from JSON file
    data = load_data()
    
    # find patient by id
    if patient_id in data:
        return data[patient_id]
    raise HTTPException(status_code=404, detail='Patient not found')







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








# define update endpoint
@app.put("/edit/{patient_id}")
def update_patient(patient_id: str, patient_update: PatientUpdate):
    
    # load existing patients from a database or file (simulated here with a list)
    data = load_data()
    
    # Check if patient with given ID exists
    if patient_id not in data:
        raise HTTPException(status_code=404, detail="Patient with this ID does not exist")  
    
    
    # update patient details
    existing_patient_data = data[patient_id]
    
    updated_data = patient_update.model_dump(exclude_unset=True)
    
    for key, value in updated_data.items():
        existing_patient_data[key] = value
    
    # Recalculate BMI and BMI category if height or weight is updated
    if 'height' in updated_data or 'weight' in updated_data:
        height = existing_patient_data.get('height', 0)
        weight = existing_patient_data.get('weight', 0)
        if height > 0 and weight > 0:
            bmi = weight / ((height / 100) ** 2)
            existing_patient_data['bmi'] = bmi
            if bmi < 18.5:
                existing_patient_data['bmi_category'] = "Underweight"
            elif 18.5 <= bmi < 24.9:
                existing_patient_data['bmi_category'] = "Normal weight"
            elif 25 <= bmi < 29.9:
                existing_patient_data['bmi_category'] = "Overweight"
            else:
                existing_patient_data['bmi_category'] = "Obesity"
    
    data[patient_id] = existing_patient_data
    
    # Save the updated data back to the JSON file
    save_data(data)
    
    return JSONResponse(status_code=200, content={"message": "Patient updated successfully"})









# define delete endpoint
@app.delete("/delete/{patient_id}")
def delete_patient(patient_id: str):
    
    # load existing patients from a database or file (simulated here with a list)
    data = load_data()
    
    # Check if patient with given ID exists
    if patient_id not in data:
        raise HTTPException(status_code=404, detail="Patient with this ID does not exist")  
    
    
    # delete patient details
    del data[patient_id]
    
    # Save the updated data back to the JSON file
    save_data(data)
    
    return JSONResponse(status_code=200, content={"message": "Patient deleted successfully"}) 