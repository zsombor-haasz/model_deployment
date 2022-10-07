import streamlit as st

st.set_page_config(
    page_title = 'Streamlit Presentation',
    page_icon = '🍻'
)

st.image('streamlit.png', width = 300)
st.title('What is Streamlit?')
st.markdown('''
* An open-source framework to build beautiful data apps in Python
* Released in 2019, acquired by Snowflake in 2022
''')

ok = st.button('Let it snow!')
if ok:
    st.snow()

st.title('Why use Streamlit?')

st.markdown('''
* Streamlit focuses on simplicity: the fastest way to build and share data apps
* Streamlit is beautiful
* Streamlit is very good for quick prototyping
''')


st.title('How to use Streamlit?')
st.write('Install streamlit:')
st.code('$ pip install streamlit')
st.write('''Write your python script in *my_app.py* and run the web app:''')
st.code('$ streamlit run my_app.py')

#st.write('Ok, but what does the script look like?')
with st.expander("Ok, but what does the script look like?"):
    st.code('''
import streamlit as st

st.set_page_config(
    page_title = 'Streamlit Presentation',
    page_icon = '🍻'
)

st.title('What is Streamlit?')
st.markdown(\'''
* An open-source framework to build beautiful data apps in Python
* Released in 2019, acquired by Snowflake in 2022
\''')

ok = st.button('Let it snow!')
if ok:
    st.snow()

st.title('Why Streamlit?')

st.markdown(\'''
* Streamlit focuses on simplicity: *"How can we make a machine learning script \n and convert it into an app as simple as possible, so that it basically feels \nlike a scripting exercise?"* - Inventor of Streamlit, Adrien Treuille (Ph.D.)
* Streamlit is beautiful
\''')

st.title('How to use Streamlit?')
st.write('Install streamlit:')
st.code('$ pip install streamlit')
st.write(\'''Write your python script in *my_app.py* and run the web app:\''')
st.code('$ streamlit run my_app.py')

st.write('Ok, but what does the script look like?')
''')