from pydantic import BaseModel, EmailStr, field_validator
from typing import List, Dict, Optional

# Create a Pydantic model for a Patient Step 1
class Patient(BaseModel):
    name: str
    age: int
    email: EmailStr# added email field
    weight: float = 0.0
    married: Optional[bool] = None
    allergies: List[str] = []
    contact_details: Dict[str, str] = {}
    
# 1st use of field validator for validation
    @field_validator('email', mode='before') # validate before standard validation or type conversion
    @classmethod
    def validate_email(cls, value: str):
        valid_domains = ['gmail.com', 'yahoo.com', 'outlook.com']
        domain_name = value.split('@')[-1]
        
        if domain_name not in valid_domains:
            raise ValueError(f"Email domain must be one of {valid_domains}")
        return value

# 2nd use of field validator for transformation    
    @field_validator('name')
    @classmethod
    def validate_name(cls, value: str):
        return value.upper() # convert name to uppercase transformation
    
# Create an instance of the Patient model Step 2    
Patient_info = {
    'name': "John Doe",
    'age': 30,
    'email': 'a@gmail.com',   # now valid field
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
    return patient.model_dump()

# Update the instance to verify Step 4
def update_patient(patient: Patient, updates: dict):
    updated_data = patient.model_dump()
    updated_data.update(updates)
    return updated_data

print("Insert:", insert_patient(ob1))
print("Update:", update_patient(ob1, {"age": 31}))
