import streamlit as st

st.set_page_config(
    page_title = 'Streamlit Presentation',
    page_icon = '🍻'
)


st.title('Deploy your application')
st.markdown('''
* You can deploy a standalone Streamlit app on Streamlit Cloud
* You can deploy a Streamlit app, a machine learning model or a full-fledged web application on Heroku, AWS, Azure, Google Cloud Platform, etc.
''')

st.markdown(
    '''### Google Cloud Platform
1. Download and initialize **Google Cloud CLI**

        $ gcloud init
       $ gcloud auth login
2. Publish the Docker image to **Google Container Registry**
    * with **docker push**: 
        
            $ gcloud auth configure-docker
          $ docker tag [IMAGE] gcr.io/[PROJECT-ID]/[IMAGE]
          $ docker push gcr.io/[PROJECT-ID]/[IMAGE]

    * with **Cloud Build**:
            
            $ gcloud builds submit --region=us-west2 --tag gcr.io/project-id/image-name .
3. Deploy a new service with **Cloud Run**

            $ gcloud run deploy --image gcr.io/project-id/image-name --port=8501
    ''')
