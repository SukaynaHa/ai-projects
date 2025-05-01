# app.py
import streamlit as st
import joblib
import numpy as np

# تحميل النموذج
model = joblib.load("model.pkl")
features = ['weight', 'height', 'Systolic', 'age', 'Diastolic', 'cholesterol', 'BMI', 'Family_History']

st.title("🔍 توقع خطر النوبة القلبية")

# مدخلات المستخدم لكل سمة
weight = st.number_input("الوزن (kg)", 30.0, 200.0, 70.0)
height = st.number_input("الطول (cm)", 100.0, 220.0, 170.0)
systolic = st.slider("الضغط الانقباضي (Systolic)", 90, 200, 120)
diastolic = st.slider("الضغط الانبساطي (Diastolic)", 50, 130, 80)
age = st.slider("العمر", 18, 100, 40)
cholesterol = st.slider("الكوليسترول", 100, 400, 200)
bmi = st.number_input("مؤشر كتلة الجسم (BMI)", 10.0, 60.0, 25.0)
family_history = st.selectbox("هل هناك تاريخ عائلي لأمراض القلب؟", ["لا", "نعم"])
family_history_val = 1 if family_history == "نعم" else 0

# تحويل المدخلات إلى ترتيب القائمة المطلوبة
input_data = np.array([[weight, height, systolic, age, diastolic, cholesterol, bmi, family_history_val]])

# توقع عند الضغط على الزر
if st.button("🔎 توقع الآن"):
    prediction = model.predict(input_data)[0]
    
    if prediction == 1:
        st.error("⚠️ هناك خطر مرتفع للإصابة بنوبة قلبية")
    else:
        st.success("✅ الخطر منخفض للإصابة بنوبة قلبية")
