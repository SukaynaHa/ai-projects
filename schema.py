from pydantic import BaseModel

class HeartDiseaseInput(BaseModel):
    weight: float
    height: float
    Systolic: int
    Diastolic: int
    age: int
    cholesterol: int 
    gluc: int     
    Family_History: int  
    gender: int  
    smoke: int       
    activity_level: int 

    