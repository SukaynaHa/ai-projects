from fastapi import FastAPI
from schema import HeartDiseaseInput
import numpy as np
import joblib


app = FastAPI()
# Load model
model = joblib.load("heart_disease_model.pkl")

@app.post("/predict")
async def predict(data: HeartDiseaseInput):

    # Calculate BMI
    height_m = data.height / 100
    bmi_raw = data.weight / (height_m ** 2)

    if bmi_raw <= 18.4:
        BMI = 1
    elif bmi_raw < 25:
        BMI = 2
    elif bmi_raw < 30:
        BMI = 3
    elif bmi_raw < 40:
        BMI = 4
    else:
        BMI = 5

    # BMI-Activity
    BMI_activity = BMI * (1 - data.activity_level)

    # Prepare input for model
    input_data = np.array([[data.weight, data.height, data.Systolic, data.age, data.Diastolic,
                            data.cholesterol, BMI, data.Family_History, data.gender, BMI_activity, data.gluc, data.smoke]])


    # Make prediction
    prediction = model.predict(input_data)
    probability = model.predict_proba(input_data)[0][1]  # Use predict_proba for probability
    health_risk = "High" if prediction[0] == 1 else "Low"

   
    return {
        "health_risk": health_risk,
        "probability": float(probability)  
    }



