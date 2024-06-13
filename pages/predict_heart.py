import streamlit as st
import pymysql
import pickle
import numpy as np

#def sql_connector():
#    conn = pymysql.connect(user = 'root', password = 'root', db = 'patient_infos', host = 'localhost')
#    c = conn.cursor()
#    return conn, c

model_diabetes = pickle.load(open("heart.pkl", "rb"))

def prepare_model(input_vars):
    input_data_as_np_array = np.asarray(input_vars)
    input_data_reshaped = input_data_as_np_array.reshape(1,-1)
    prediction = model_diabetes.predict(input_data_reshaped)
    if(prediction[0] == 0):
        st.write("You don't have heart disase...")
    else:
        st.write("You have heart disase... Sometimes expert opinion is important. To get support our chatbot: ")
        st.markdown("[Chatbot](/chatbot)")

st.title("Heart Disase Prediction")
st.markdown("""If you know anything about input variables please visit the [Heart Page](/heart)""")
age = float(st.number_input("Age", min_value = 0, max_value = 100, step = 1))
gender = st.radio("Gender", ["Male", "Female"])
gender = 1.0 if gender == "Yes" else 0.0
vars = ["1-Low","2-Mid","3-Much"]
cp = st.selectbox("CP", vars)
if cp == "1-Low":
    cp = 1.0
elif cp == "2-Mid":
    cp = 2.0
else:
    cp = 3.0
trestbps = float(st.number_input("Trest BPS", min_value=0, max_value=300))
chol = float(st.number_input("Chol", min_value=0, max_value= 1000))
fbs = st.radio("Fbs (Under 120 mg/dl) ", ["No", "Yes"])
fbs = 1.0 if fbs == "Yes" else 0.0
rest_ecg = float(st.number_input("Rest Ecg", min_value=1, max_value= 3))
thalach = float(st.number_input("Thalach", min_value=0, max_value= 1000))
exang = st.radio("Exang ", ["Angina Available", "Angina Nonavailable"])
exang = 1.0 if exang == "Angina Available" else 0.0
oldpeak = float(st.number_input("Oldpeak", min_value=0, max_value=1000))
slope = float(st.number_input("Slope", min_value=0, max_value=3))
ca = float(st.number_input("Ca", min_value=0, max_value=1000))
thal = float(st.number_input("Thal", min_value=0, max_value=3))
button = st.button("Predict")

if button:
    #conn, c = sql_connector()
    #c.execute("INSERT INTO patients (age,gender,cp,trestbps,chol,fbs,rest_ecg,thalach,exang,oldpeak,slope,ca,thal) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (age,gender,cp,trestbps,chol,fbs,rest_ecg,thalach,exang,oldpeak,slope,ca,thal))
    #conn.commit()
    #conn.close()
    #c.close()
    prepare_model([age,gender,cp,trestbps,chol,fbs,rest_ecg,thalach,exang,oldpeak,slope,ca,thal])