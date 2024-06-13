import streamlit as st
import pymysql
import pickle
import numpy as np

#def sql_connector():
#    conn = pymysql.connect(user = 'root', password = 'root', db = 'patient_infos', host = 'localhost')
#    c = conn.cursor()
#    return conn, c

model_diabetes = pickle.load(open("diabetes.pkl", "rb"))

def prepare_model(input_vars):
    input_data_as_np_array = np.asarray(input_vars)
    input_data_reshaped = input_data_as_np_array.reshape(1,-1)
    prediction = model_diabetes.predict(input_data_reshaped)
    if(prediction[0] == 0):
        st.write("You don't have diabetes...")
    else:
        st.write("You have diabetes... Sometimes expert opinion is important. To get support our chatbot: ")
        st.markdown("[Chatbot](/chatbot)")

st.title("Diabetes Prediction")
st.markdown("""If you know anything about input variables please visit the [Diabetes Page](/diabetes)""")
high_bp = st.radio("Please choose your bp", ["Low", "High"])
high_bp = 1.0 if high_bp == "High" else 0.0
high_chol = st.radio("Please choose your cholesterol", ["Low", "High"])
high_chol = 1.0 if high_chol == "High" else 0.0
chol_check = st.radio("Please choose your check of your cholesterol", ["Low", "High"])
chol_check = 1.0 if chol_check == "High" else 0.0
bmi = float(st.number_input("Please enter your bmi score", min_value=5, max_value=40))
smoke = st.radio("Do you smoke ? ", ["No", "Yes"])
smoke = 1.0 if smoke == "Yes" else 0.0
stroke = st.radio("Do you have a stroke?", ["No", "Yes"])
stroke = 1.0 if high_bp == "Yes" else 0.0
heart_disase_or_heart_attack = st.radio("Have you ever been hit by a heart attack or heart disase?", ["No", "Yes"])
heart_disase_or_heart_attack = 1.0 if heart_disase_or_heart_attack == "Yes" else 0.0
phys_activity = st.radio("Phys activity", ["No", "Yes"])
phys_activity = 1.0 if phys_activity == "Yes" else 0.0
fruits = st.radio("Do you eat fruits regularly?", ["No", "Yes"])
fruits = 1.0 if fruits == "Yes" else 0.0
veggies = st.radio("Do you eat vegetables regularly?", ["No", "Yes"])
veggies = 1.0 if veggies == "Yes" else 0.0
hvy_alcohol_consump = st.radio("Do you have heavy alcohol consumption?", ["No", "Yes"])
hvy_alcohol_consump = 1.0 if hvy_alcohol_consump == "Yes" else 0.0
any_healthcare = st.radio("Do you have any health care?", ["No", "Yes"])
any_healthcare = 1.0 if any_healthcare == "Yes" else 0.0
no_doc_bc_cost = st.radio("No doc by cost?", ["No", "Yes"])
no_doc_bc_cost = 1.0 if no_doc_bc_cost == "Yes" else 0.0
gen_health = float(st.number_input("Gen Health", min_value=1, max_value=100))
mental_health = float(st.number_input("Mental Health", min_value=1, max_value=100))
phys_hlth = float(st.number_input("Physical Health", min_value=1, max_value=100))
diff_walk = st.radio("Diff Walk", ["No", "Yes"])
diff_walk = 1.0 if diff_walk == "Yes" else 0.0
gender = st.radio("Gender", ["Male", "Female"])
gender = 1.0 if gender == "Yes" else 0.0
age = float(st.number_input("Age", min_value = 0, max_value = 100, step = 1))
button = st.button("Predict")

if button:
    #conn, c = sql_connector()
    #c.execute("INSERT INTO patients (high_bp,high_chol,chol_check,bmi,smoke,stroke,heart_disase_or_heart_attack,phys_activity,fruits,veggies,hvy_alcohol_consump,any_healthcare,no_doc_bc_cost,gen_health,mental_health,phys_hlth,diff_walk,gender,age ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (high_bp,high_chol,chol_check,bmi,smoke,stroke,heart_disase_or_heart_attack,phys_activity,fruits,veggies,hvy_alcohol_consump,any_healthcare,no_doc_bc_cost,gen_health,mental_health,phys_hlth,diff_walk,gender,age))
    #conn.commit()
    #conn.close()
    #c.close()
    prepare_model([high_bp,high_chol,chol_check,bmi,smoke,stroke,heart_disase_or_heart_attack,phys_activity,fruits,veggies,hvy_alcohol_consump,any_healthcare,no_doc_bc_cost,gen_health,mental_health,phys_hlth,diff_walk,gender,age])