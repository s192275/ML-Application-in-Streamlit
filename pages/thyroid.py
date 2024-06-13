import streamlit as st
st.title("Information About Thyroid Disase Prediction API")
st.write(
    """
    This is an ML API used for predicting the probability of having Thyroid Disase by Classification. The API is created by Serhat KILIÇ.
    This dataset was obtained from Kaggle(Thyroid Disease Data ).
""")
st.markdown("""To Reach [Dataset](https://www.kaggle.com/datasets/yasserhessein/thyroid-disease-data-set)""")    
st.write("""About ML API""")
st.markdown("First, you must fill in all the blanks, radio buttons, and other components of the API. If you know the all inputs and what they are please visit the [Predict](/predict_thyroid)""")
st.write("""
Explanation About Inputs

Age: Age of patient.

Sex: Gender of patient.

On Thyroxine: Does patient receive thyroid hormone therapy?

Query on Thyroxine: Does patient have query about thyroxine?

Antithyroid Medication: Does patient receive antithyroid medication?

Sick: Does patient sick?

Pregnant: Does patient pregnant?

Thyroid Surgery: Has the patient had thyroid surgery before?

I131 Treatment: Does patient receive I131 threatment?

Query Hypothyroid: Does patient have query about hypothyroid?

Query Hyperthyroid: Does patient have query about hyperthyroid?

Lithium: Does patient use lithium pills?

Goitre: Does patient have goitre?

Hypopituitary: Does patients hypopituitary works normally?

Psych: Psychological value

TSH: TSH value

T3: T3 value

TT4: TT4 value

T4U: T4U value

Referral Source: Categories(Other-SVI-SVHC-STMW-SVHD)
""")