from pydantic import BaseModel, Field, field_validator
from typing import Literal, Annotated


# Input schema
class UserInput(BaseModel):
    age: Annotated[int, Field(gt=0, lt=120, description="Age must be between 1 and 119")]
    sex: Annotated[Literal['male', 'female'], Field(description="Gender of the person")]
    bmi: Annotated[float, Field(gt=0, lt=100, description="BMI must be between 0 and 100")]
    children: Annotated[int, Field(ge=0, lt=20, description="Number of children between 0 and 19")]
    smoker: Annotated[Literal['yes', 'no'], Field(description="Smoker: yes or no")]
    region: Annotated[Literal['northeast', 'northwest', 'southeast','southwest'], Field(description="Region must be one of: northeast, northwest, southeast, southwest")]
    
    @field_validator('region', 'sex', 'smoker', mode="before")
    @classmethod
    def normalize_lower(cls, value: str) -> str:
        return value.lower()
