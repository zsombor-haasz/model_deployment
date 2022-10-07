import streamlit as st

st.set_page_config(
    page_title = 'Streamlit Presentation',
    page_icon = '🍻'
)


st.title('Summary')
a,b =st.columns(2)
with a:
    st.markdown('''1. Build a web application:
*   **Flask** - *with HTML, CSS and JavaScript*
*   **Dash** - *specifically for data apps*
*   **Streamlit** - *fast and simple*''')


with b:
    st.markdown('''
2. Serve the model:
*   **Flask** - *a general micro web framework*
*   **MLflow** - *with tracking & model registry services*
*   **BentoML** - *specifically for ML deployment*
''')
st.markdown('3. Containerize the services (**Docker**, **Kubernetes**) and deploy them to the cloud (Heroku, AWS, Azure, GCP)')