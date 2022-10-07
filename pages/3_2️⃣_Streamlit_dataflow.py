import streamlit as st

st.set_page_config(
    page_title = 'Streamlit Presentation',
    page_icon = '🍻'
)

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
st.write(f'Your name from the previous page is: {st.session_state["shared_name"]}')
