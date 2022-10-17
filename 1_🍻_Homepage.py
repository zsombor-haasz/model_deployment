import streamlit as st

st.set_page_config(
    page_title = 'Streamlit Presentation',
    page_icon = '🍻'
)

st.title('Model Deployment with Streamlit, MLflow and Docker')

st.markdown('''
1. Make a web app that looks cool (Streamlit)
2. Separate the machine learning model from the web app (Flask / MLflow / BentoML)
3. Track the model development steps (MLflow)
3. Make it easy to share the app (MLflow, Docker)
4. Deploy to the cloud (GCP, AWS, AZure)''')