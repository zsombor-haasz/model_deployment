import streamlit as st

st.set_page_config(
    page_title = 'Streamlit Presentation',
    page_icon = '🍻'
)


st.title('What is Gradio?')
st.markdown('''
Gradio is the fastest way to demo your machine learning model with a friendly web interface so that anyone can use it, anywhere!
''')

st.title('How to use Gradio?')
st.write('''
* In Jupyter Notebook
* In the browser on http://localhost:7860
* A Gradio interface can automatically generate a public link you can share with colleagues that lets them interact with the model on your computer remotely from their own devices.
* Upload to Hugging Face. For example: https://huggingface.co/spaces/akhaliq/JoJoGAN
''')

