import streamlit as st

st.set_page_config(
    page_title = 'Streamlit Presentation',
    page_icon = '🍻'
)

if 'shared_name' not in st.session_state:
    st.session_state['shared_name'] = ''

st.markdown('''# [Churn Prediction Model Results](http://localhost:8501)''')
