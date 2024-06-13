import streamlit as st
st.title("Information About Diabetes Prediction API")
st.write("""
This is an ML API used for predicting the probability of having diabetes by Classification. The API is created by Serhat KILIÇ.

This dataset was obtained from UCI Machine Learning Repository(CDC Diabetes Health Indicators).
""")

st.markdown("""To Reach [Dataset](https://archive.ics.uci.edu/dataset/891/cdc+diabetes+health+indicators)""")

st.write(
"""About ML API

First, you must fill in all the blanks, radio buttons, and other components of the API. If you know the all inputs and what they are please visit the Predict

Explanation About Inputs:

HighBP: High blood pressure (Categorical(0-1))

HighChol: High chol (Categorical(0-1))

CholCheck: Checking of cholestrol.(Categorical(0-1))

BMI: Body Mass Index(Numerical)

Smoker: Smoking habit(Categorical(0-1))

Stroke: Categorical(0-1)

Heart Disase or Heart Attack: Heart Disase(Categorical(0-1))

Physical Activity: Patient's physical activity(Categorical(0-1))

Fruits: Does patient eat fruits regularly?(Categorical(0-1))

Veggies: Does patient eat vegetables regularly? (Categorical(0-1))

Heavy Alcohol Consumption: Alcohol consumption (Categorical(0-1))

Any Healthcare: Healthcare none or available(Categorical(0-1))

NoDocbcCost: Categorical(0-1)

GenHlth: Genetical Health(Categorical(1-2-3-4-5))

MentHlth: Mental Health.(Numeric)

PhysHlth: Physical Health.(Numeric)

DiffWalk: It represents walking habits.(0-1)

Sex: Gender of patient

Age: Age of the patient
""")
st.markdown("""
            If you know all variables please visit the [Predict Page](/predict_diabetes)""")
