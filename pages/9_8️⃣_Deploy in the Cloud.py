import streamlit as st

st.set_page_config(
    page_title = 'Streamlit Presentation',
    page_icon = '🍻'
)


st.title('Deploy your application')
st.markdown('''
* Deploy the standalone Streamlit app:
    * on Streamlit Cloud
    * on other hosting services (Heroku, AWS, Azure, GCP etc.)
* Deploy the containerized application (Heroku, AWS, Azure, GCP etc.)
''')
