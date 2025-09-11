from pydantic import BaseModel, model_validator
from typing import List, Dict, Optional

# Create a Pydantic model for a Patient Step 1
class Patient(BaseModel):
    name: str
    age: int
    weight: float = 0.0 # default value
    married: Optional[bool] = None
    allergies: List[str] = []
    contact_details: Dict[str, str] = {}
    emergency_contact: Optional[str] = None
    
    # model validator for validation
    @model_validator(mode='after') # validate after standard validation or type conversion
    
    def validate_emargency_contact(cls, model):
        if model.age > 60 and 'emergency' not in model.contact_details:
            raise ValueError("Emergency contact is required for patients over 60")
           
        return model
    
# Create an instance of the Patient model Step 2    
Patient_info = {
    'name': "John Doe",
    'age': 30,
    'weight': 70.5,
    'married': True,
    'allergies': ['pollen', 'nuts'],
    'contact_details': {
        'email': 'a@gmail.com',
        'phone': '123-456-7890',
        'emergency': '987-654-3210'
    }
} 


ob1 = Patient(**Patient_info)

# Insert the instance to verify Step 3
def insert_patient(patient: Patient):
    # Simulate inserting patient into a database
    return patient.model_dump()

# Update the instance to verify Step 4
def update_patient(patient: Patient, updates: dict):
    # Simulate updating patient in a database
    updated_data = patient.model_dump()
    updated_data.update(updates)
    return updated_data

print("Insert:", insert_patient(ob1))

# Example update: changing age
print("Update:", update_patient(ob1, {"age": 31}))
