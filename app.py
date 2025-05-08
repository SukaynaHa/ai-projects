# import streamlit as st
# import joblib
# import numpy as np

# model = joblib.load("heart_disease_model.pkl")


# # إضافة صورة

# st.image("C:/Users/Sakena/Desktop/ai-projects/heart-attack-prediction/heartimage.png", caption="Welcome to Heart Disease Prediction", width=200)


# # عنوان التطبيق
# st.title("Heart Disease Risk Prediction 🔍")



# st.write("أدخل البيانات التالية:")


# # مدخلات المستخدم
# weight = st.number_input("Weight (kg)", min_value=30.0, max_value=200.0, value=70.0)
# height = st.number_input("Height (cm)", min_value=100.0, max_value=250.0, value=170.0)
# # systolic = st.number_input("Systolic Blood Pressure", min_value=80, max_value=250, value=120)
# # diastolic = st.number_input("Diastolic Blood Pressure", min_value=40, max_value=150, value=80)
# systolic = st.slider("الضغط الانقباضي (Systolic)", 80, 200, 120)
# diastolic = st.slider("الضغط الانبساطي (Diastolic)", 40, 150, 80)
# age = st.number_input("Age", min_value=1, max_value=120, value=30)

# # نصوص ثم تحويلها إلى أرقام
# cholesterol_text = st.selectbox("Cholesterol Level", ["normal", "above_normal", "well_above_normal"])
# gluc_text = st.selectbox("Glucose Level", ["normal", "above_normal", "well_above_normal"])
# family_history = st.selectbox("Family History of Heart Disease", ["No", "Yes"])
# gender = st.selectbox("Gender", ["Male", "Female"])
# smoke = st.selectbox("Do you smoke?", ["No", "Yes"])
# activity_level = st.selectbox("Are you physically active?", ["No", "Yes"])

# # تحويل القيم النصية إلى أرقام

# cholesterol_map = {"normal": 1, "above_normal": 2, "well_above_normal": 3}
# gluc_map = {"normal": 1, "above_normal": 2, "well_above_normal": 3}
# cholesterol = cholesterol_map[cholesterol_text]
# gluc = gluc_map[gluc_text]
# family_history = 1 if family_history == "Yes" else 0
# gender = 1 if gender == "Male" else 0
# smoke = 1 if smoke == "Yes" else 0
# activity_level = 1 if activity_level == "Yes" else 0
# # حساب BMI الخام
# height_m = height / 100
# bmi_raw = weight / (height_m ** 2)

# # تصنيف BMI إلى فئة (1 إلى 5)
# if bmi_raw <= 18.4:
#     bmi = 1
# elif bmi_raw < 25:
#     bmi = 2
# elif bmi_raw < 30:
#     bmi = 3
# elif bmi_raw < 40:
#     bmi = 4
# else:
#     bmi = 5

# # حساب BMI_activity
# bmi_activity = bmi * (1 - activity_level)

# # عرض النتائج المحسوبة
# st.markdown(f"**BMI :** {bmi_raw:.2f}")
# st.markdown(f"**BMI catigory :** {bmi}")
# st.markdown(f"**BMI Activity:** {bmi_activity:.2f}")

# # إنشاء مصفوفة الإدخال للنموذج
# input_data = np.array([[weight, height, systolic, age, diastolic, cholesterol,
#                         bmi, family_history, gender, bmi_activity, gluc, smoke]])





# # تنسيق الزر باستخدام Markdown وCSS
# st.markdown("""
#     <style>
#     .predict-button {
#         background-color: #4CAF50;
#         color: white;
#         padding: 0.6em 1.2em;
#         border: none;
#         border-radius: 8px;
#         font-size: 18px;
#         cursor: pointer;
#         transition: background-color 0.3s ease;
#     }

#     .predict-button:hover {
#         background-color: #45a049;
#     }

#     .result-box {
#         padding: 20px;
#         border-radius: 10px;
#         font-size: 18px;
#         font-weight: bold;
#         margin-top: 20px;
#     }

#     .risk-high {
#         background-color: #ffdddd;
#         border-left: 6px solid #f44336;
#         color: #b30000;
#     }

#     .risk-low {
#         background-color: #ddffdd;
#         border-left: 6px solid #4CAF50;
#         color: #006600;
#     }
#     </style>
# """, unsafe_allow_html=True)

# # الزر
# if st.button("🔎 توقع الآن", key="predict_button"):
#     prediction = model.predict(input_data)[0]
#     proba = model.predict_proba(input_data)[:, 1]

#     if prediction == 1:
#       st.markdown("""
#         <div class="result-box risk-high">
#             ⚠️ <strong>تنبيه:</strong> هناك خطر <u>مرتفع</u> للإصابة بنوبة قلبية.
#         </div>
#     """, unsafe_allow_html=True)
#     else:
#          st.markdown("""
#         <div class="result-box risk-low">
#             ✅ <strong>ممتاز:</strong> الخطر <u>منخفض</u> للإصابة بنوبة قلبية.
#         </div>
#     """, unsafe_allow_html=True)



# # Without HTML

# # if st.button("Predict"):
# #     prediction = model.predict(input_data)
# #     proba = model.predict_proba(input_data)[:, 1]

# #     if prediction[0] == 1:
# #         st.error(f"⚠️ خطر مرتفع للإصابة بأمراض القلب (احتمالية: {proba[0]:.2f})")
# #     else:
# #         st.success(f"✅ خطر منخفض للإصابة بأمراض القلب (احتمالية: {proba[0]:.2f})")



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
