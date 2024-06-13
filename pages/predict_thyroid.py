import streamlit as st
import pymysql
import pickle
import numpy as np

#def sql_connector():
#    conn = pymysql.connect(user = 'root', password = 'root', db = 'patient_infos', host = 'localhost')
#    c = conn.cursor()
#    return conn, c

model_diabetes = pickle.load(open("thyroid.pkl", "rb"))

def prepare_model(input_vars):
    input_data_as_np_array = np.asarray(input_vars)
    input_data_reshaped = input_data_as_np_array.reshape(1,-1)
    prediction = model_diabetes.predict(input_data_reshaped)
    if(prediction[0] == 0):
        st.write("You don't have thyroid disase...")
    else:
        st.write("You have thyroid disase... Sometimes expert opinion is important. To get support our chatbot: ")
        st.markdown("[Chatbot](/chatbot)")

st.title("Thyroid Disase Prediction")
st.markdown("""If you know anything about input variables please visit the [Thyroid Page](/thyroid)""")
age = float(st.number_input("Age", min_value = 0, max_value = 100, step = 1))
gender = st.radio("Gender", ["Male", "Female"])
gender = 1.0 if gender == "Yes" else 0.0
on_thyroxine = st.radio("On Thyroxine", ["No", "Yes"])
on_thyroxine = 1.0 if on_thyroxine == "Yes" else 0.0
query_on_thyroxine = st.radio("Query On Thyroxine", ["No", "Yes"])
query_on_thyroxine = 1.0 if query_on_thyroxine == "Yes" else 0.0
bmi = float(st.number_input("Please enter your bmi score", min_value=5, max_value=40))
on_antithyroid_medication = st.radio("On Antithyroid Medication ", ["No", "Yes"])
on_antithyroid_medication = 1.0 if on_antithyroid_medication == "Yes" else 0.0
sick = st.radio("Sick ", ["No", "Yes"])
sick = 1.0 if sick == "Yes" else 0.0
pregnant = st.radio("Pregnant ", ["No", "Yes"])
pregnant = 1.0 if pregnant == "Yes" else 0.0
thyroid_surgery = st.radio("Have you ever had thyroid surgery ? ", ["No", "Yes"])
thyroid_surgery = 1.0 if thyroid_surgery == "Yes" else 0.0
i131_treatment = st.radio("Have you ever taken I131 Treatment", ["No", "Yes"])
i131_treatment = 1.0 if i131_treatment == "Yes" else 0.0
query_hypothyroid = st.radio("Query Hypothyroid", ["No", "Yes"])
query_hypothyroid = 1.0 if query_hypothyroid == "Yes" else 0.0
query_hyperthyroid =  st.radio("Query Hyperthyroid", ["No", "Yes"])
query_hyperthyroid = 1.0 if query_hyperthyroid == "Yes" else 0.0
lithium = st.radio("Do you use lithium ? ", ["No", "Yes"])
lithium = 1.0 if lithium == "Yes" else 0.0
hypopituitary = st.radio("Hypopituitary", ["No", "Yes"])
hypopituitary = 1.0 if hypopituitary == "Yes" else 0.0
goitre = st.radio("Do you have goitre ?", ["No", "Yes"])
goitre = 1.0 if goitre == "Yes" else 0.0
phys = st.radio("Phys", ["No", "Yes"])
phys = 1.0 if phys == "No" else 0.0
tsh = float(st.number_input("TSH", min_value=0, max_value=100))
t3 = float(st.number_input("T3", min_value=1, max_value=100))
t4u = float(st.number_input("T4U", min_value=1, max_value=100))
vars = ["Other","SVHC","SVI","STMW","SVHD"]
referral_source = st.selectbox("Referral Source", vars)
if referral_source == "Other":
    referral_source = 1.0
elif referral_source == "SVHC":
    referral_source = 2.0
elif referral_source == "SVI":
    referral_source = 3.0
elif referral_source == "STMV":
    referral_source = 4.0
else:
    referral_source = 5.0
button = st.button("Predict")

if button:
    #conn, c = sql_connector()
    #c.execute("INSERT INTO patients (age,gender,on_thyroxine,query_on_thyroxine,bmi,on_antithyroid_medication,sick,pregnant,thyroid_surgery,i131_treatment,query_hypothyroid,query_hyperthyroid,lithium,hypopituitary,goitre,phys,tsh,t3,t4u,referral_source ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (age,gender,on_thyroxine,query_on_thyroxine,bmi,on_antithyroid_medication,sick,pregnant,thyroid_surgery,i131_treatment,query_hypothyroid,query_hyperthyroid,lithium,hypopituitary,goitre,phys,tsh,t3,t4u,referral_source))
    #conn.commit()
    #conn.close()
    #c.close()
    prepare_model([age,gender,on_thyroxine,query_on_thyroxine,bmi,on_antithyroid_medication,sick,pregnant,thyroid_surgery,i131_treatment,query_hypothyroid,query_hyperthyroid,lithium,hypopituitary,goitre,phys,tsh,t3,t4u,referral_source])