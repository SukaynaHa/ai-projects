import streamlit as st
import requests
from fastapi import FastAPI

app = FastAPI() 



# عنوان التطبيق
st.title("Heart Disease Risk Prediction 🔍")
#-------------------------------------------------------------------------------------
import base64

def get_base64_image(image_path):
    with open(image_path, "rb") as image_file:
        encoded = base64.b64encode(image_file.read()).decode()
    return f"data:image/jpeg;base64,{encoded}"

image_path = "images/imgHeart.png"
base64_image = get_base64_image(image_path)

st.markdown(f"""
    <style>
    .stApp {{
        background-image: url("{base64_image}");
        background-size: cover;
        background-repeat: no-repeat;
        background-position: center;
    }}
    </style>
""", unsafe_allow_html=True)



#-------------------------------------------------------------------------------------


st.write("**Enter information :**")

# جمع المدخلات من المستخدم
weight = st.number_input("**Weight (kg)**", min_value=30.0, max_value=200.0, value=70.0)
height = st.number_input("**Height (cm)**", min_value=100.0, max_value=250.0, value=170.0)
Systolic = st.slider("**Systolic Blood Pressure**", 80, 200, 120)
Diastolic = st.slider("**Diastolic Blood Pressure**", 40, 150, 80)
age = st.number_input("**Age**", min_value=1, max_value=120, value=30)
cholesterol_text = st.selectbox("**Cholesterol Level**", ["Normal", "Above Normal", "Well Above Normal"])
gluc_text = st.selectbox("**Glucose Level**", ["Normal", "Above Normal", "Well Above Normal"])
Family_History = st.selectbox("**Family History of Heart Disease**", ["No", "Yes"])
gender = st.selectbox("**Gender**", ["Male", "Female"])
smoke = st.selectbox("**Do you smoke?**", ["No", "Yes"])
activity_level = st.selectbox("**Are you physically active?**", ["No", "Yes"])



# تحويل المدخلات النصية إلى أرقام
cholesterol_map = {"Normal": 1, "Above Normal": 2, "Well Above Normal": 3}
gluc_map = {"Normal": 1, "Above Normal": 2, "Well Above Normal": 3}
cholesterol = cholesterol_map[cholesterol_text]
gluc = gluc_map[gluc_text]
Family_History = 1 if Family_History == "Yes" else 0
gender = 1 if gender == "Male" else 0
smoke = 1 if smoke == "Yes" else 0
activity_level = 1 if activity_level == "Yes" else 0

input_data = {
    "weight": weight,
    "height": height,
    "Systolic": Systolic,
    "Diastolic": Diastolic,
    "age": age,
    "cholesterol": cholesterol,
    "gluc": gluc,
    "Family_History": Family_History,
    "gender": gender,
    "smoke": smoke,
    "activity_level": activity_level
}

if st.button("🔎 **PREDICT** "):
    response = requests.post("http://127.0.0.1:8000/predict", json=input_data)#post to fastapi

    if response.status_code == 200:
        result = response.json()
        health_risk = result["health_risk"]
        probability = result["probability"]

        if health_risk == "High":
            st.markdown(f"⚠️ **High risk of heart attack** with probability : ({probability:.2f})")
        else:
            st.markdown(f"✅ **Low risk of heart attack** with probability : ({probability:.2f})")
    else:
        st.error("حدث خطأ أثناء الاتصال ـ FastAPI")
