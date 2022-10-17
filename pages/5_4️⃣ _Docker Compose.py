import streamlit as st

st.set_page_config(
    page_title = 'Streamlit Presentation',
    page_icon = '🍻'
)


st.title('What is Docker Compose?')
st.write('''
Compose is a tool for defining and running multi-container Docker applications. With Compose, you use a YAML file to configure your application’s services. Then, with a single command, you create and start all the services from your configuration.''')

st.title('How to use Docker Compose?')

st.write('''
1. Define your app's environment with a **Dockerfile** so it can be reproduced anywhere.
2. Define the services that make up your app in **docker-compose.yml** so they can be run together in an isolated environment.
3. Run **docker compose up -- build** and the Docker compose command starts and runs your entire app.
''')
st.write('Note: in the POST request, you must replace localhost with the name of the other container, or host.docker.internal.')

st.markdown('### Docker-compose.yml')
with st.expander('Streamlit & Flask'):
    st.code('''
services:
  streamlit:
    container_name: streamlit_app
    build: .
    command: "streamlit run streamlit_app.py"
    ports:
      - "8501:8501"
  flask:
    container_name: flask_app
    build: .
    command: "flask run --host 0.0.0.0 --port 8080"
    ports:
     - "8080:8080"
     ''')