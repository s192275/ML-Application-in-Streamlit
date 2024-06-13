import streamlit as st
st.title("Information About Heart Disase Prediction API")
st.write("""
This is an ML API used for predicting the probability of having heart disease by Classification. The API is created by Serhat KILIÇ.
This dataset was obtained from the heart disease data set on Kaggle.
""")

st.markdown("""To Reach [Dataset](https://www.kaggle.com/datasets/yasserh/heart-disease-dataset)""")

st.write(
"""About ML API

First, you must fill in all the blanks, radio buttons, and other components of the API. If you know the all inputs and what they are please visit the Predict

Explanation About Inputs

Age: Age of the patient

Sex: Gender of the patient

Cp: Chest pain categorized by the patient (0-3)

Trestbps: Heart pulse per minute

Chol: Cholesterol of the patient

Fbs (Fasting Blood Sugar): It is 0 if it is under 120 mg/dl

Restecg: It shows resting electrocardiographic results.
    
    0: Normal
    
    1: ST-T waves anomalies
    
    2: Possible or definite left ventricular hypertrophy determined by ECG

Thalach: Maximum Heart Rate Achieved

Exang (Exercise Induced Angina): It is 0 if there is no angina due to exercise. Otherwise 1.

Oldpeak (ST Depression Induced by Exercise): It represents induced ST depression by exercise.

Slope: It represents slope of ST segment.

    0: No slope

    1: An elevated ST segment with stroke onset.
    
    2: A depressed ST segment is the onset of stroke.

Ca (Major Vessels Colored by Fluroscopy): It respresents number of big vessels colorized by fluroroscophy

Thal: It represents type of thalassemia
""")
st.markdown("""
            If you know all variables please visit the [Predict Page](/predict_heart)""")

