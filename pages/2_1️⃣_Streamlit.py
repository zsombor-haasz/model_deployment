from os import link
import streamlit as st
import datetime
import pandas as pd
import numpy as np

st.set_page_config(
    page_title = 'Streamlit Presentation',
    page_icon = '🍻'
)


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

with st.expander("Ok, but what does the script look like?"):
    st.code( ... )
''')


if 'shared_name' not in st.session_state:
    st.session_state['shared_name'] = ''

st.title('Streamlit elements')

st.write('''
* You can add text (markdown, latex) and tables
* You can add charts (built-in, matplotlib, pyplot, bokeh etc.) and images
* You can interact with the user via input widgets:
    * Button, Download button
    * Chcekbox, Radio button, Selectbox, Slider
    * Text input, Number input, File uploader
    * and many more
* You can create columns, add a sidebar, add pages

See the [documentation](https://docs.streamlit.io/) for more elements.
''')

c1, c2, c3 = st.columns(3)
with c1:
    myname = st.text_input('Your name',st.session_state['shared_name'])
    st.write(myname)
    st.session_state["shared_name"] =myname
with c2:
    color = st.color_picker('Pick A Color', '#00f900')
    st.write('The current color is', color)
with c3:
    d = st.date_input(
    "When's your birthday?",
    datetime.date(2019, 7, 6))
    st.write('Your birthday is:', d)

c1, c2 = st.columns([1,2])
with c1:
    if st.checkbox('Show dataframe'):
        st.write(pd.DataFrame({
            'first column': [1, 2, 3, 4, 5, 6],
            'second column': [10, 20, 30, 40, 50, 60]       
        }))
with c2:
    st.line_chart(pd.DataFrame(np.random.randn(20, 3), columns=['a', 'b', 'c']))


if 'shared_name' not in st.session_state:
    st.session_state['shared_name'] = ''

st.title('Streamlit data flow')

st.write('''
    * Top to bottom execution
    * Any time something must be updated on the screen, Streamlit reruns your entire script
        * the user clicks on something
        * the source files change
    ''')
st.write('## Cache')
st.write('''
    * The Streamlit cache allows your app to execute quickly even when loading data from the web, manipulating large datasets, or performing expensive computations.
    * To use the cache, wrap functions with the @st.cache decorator.
    ''')
st.code('''
@st.cache  # 👈 This function will be cached
def my_slow_function(arg1, arg2):
    # Do something really slow in here!
    return the_output
    ''')
st.write('## Pages')
st.write('''
    * You can create multiple independent pages in separate python scripts. 
    * The pages will not share their variables, but they will share *st.session_state*. 
    ''')
#st.write(f'Your name from the previous page is: {st.session_state["shared_name"]}')
