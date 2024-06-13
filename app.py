import streamlit as st


st.set_page_config(
    page_title="ML Heathcare Service App",  
    layout="centered"
)
st.title("ML Heathcare Service App")
st.write("We care your health...")

images = ['images/diabetes.jpg', 'images/heart.jpg', 'images/thyroid.jpg', 'images/chatbot.png']
texts = ['Diabetes Prediction', 'Heart Disase Prediction', 'Thyroid Disase Prediction', 'Chatbot']
links = ['diabetes', 'heart', 'thyroid', 'chatbot']
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.image(images[0], use_column_width=True)
    st.markdown(f"<div style='text-align: center;'><a href='/{links[0]}'>{texts[0]}</a></div>", unsafe_allow_html=True)

with col2:
    st.image(images[1], use_column_width=True)
    st.markdown(f"<div style='text-align: center;'><a href='/{links[1]}'>{texts[1]}</a></div>", unsafe_allow_html=True)

with col3:
    st.image(images[2], use_column_width=True)
    st.markdown(f"<div style='text-align: center;'><a href='/{links[2]}'>{texts[2]}</a></div>", unsafe_allow_html=True)

with col4:
    st.image(images[3], use_column_width=True)
    st.markdown(f"<div style='text-align: center;'><a href='/{links[3]}'>{texts[3]}</a></div>", unsafe_allow_html=True)
