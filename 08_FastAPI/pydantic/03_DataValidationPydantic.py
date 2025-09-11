#pip install pydantic
#pip install "pydantic[email]"

from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Optional, Annotated

# Create a Pydantic model for a Patient Step 1
class Patient(BaseModel):
    name: str = Field(..., min_length=2, max_length=50,) #Custom Age validation
    age: int = Field(..., gt=17, lt=40,
                     description="Age must be between 1 and 119")
                    #Custom Age validation
    
    email: EmailStr # Email validation
    linkedin_url: AnyUrl # URL validation
    weight: Annotated[float, Field(gt = 0, title='Give the age', strict = True)] # "Annotated" use for add metadata and constraints # "Strict" ensures that only float values are accepted.
    married: Optional[bool] = None
    allergies: List[str] = []
    contact_details: Dict[str, str] = {}

# Create an instance of the Patient model Step 2    
Patient_info = {
    'name': "John Doe",
    'age': 30,
    'email': 'a@gmail.com',
    'linkedin_url': 'https://www.linkedin.com/in/johndoe',
    'weight': 70.5,
    'married': True,
    'allergies': ['pollen', 'nuts'],
    'contact_details': {
        'phone': '123-456-7890'
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
