import streamlit as st

st.set_page_config(
    page_title = 'Streamlit Presentation',
    page_icon = '🍻'
)


st.title('What is Docker?')
st.markdown('''
* The most popular containerization tool released in 2013
* A container is ”a lightweight, stand-alone, executable package of a piece of software that includes everything needed to run it.”
* You can package your software codes, configutions and dependencies in a Docker image and run it as a container on any platform where Docker is installed.
''')


st.title('Why use Docker?')

st.markdown('''

* Since containers are platform-independent, you can run your software across both Windows- and Linux-based platforms
* You don't need to bother with platform dependency, configuration and version differences
* You can share your images easily on a container registry (e.g. Docker Hub, AWS ECR)
''')

st.title('How to use Docker?')
st.write('''
1. Develop your application. Install Docker.
2. Create a Dockerfile and requirements.txt.
3. Build the Docker image:
''')
st.code('$ docker build -t streamlit .')
st.write('4. Run the Docker container:')
st.code('$ docker run -p 8501:8501 streamlit')
st.write('5. Push your image to a repository.')