from os import link
import streamlit as st
import datetime
import pandas as pd
import numpy as np

st.set_page_config(
    page_title = 'Streamlit Presentation',
    page_icon = '🍻'
)

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
