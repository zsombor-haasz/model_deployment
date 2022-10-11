import streamlit as st

st.set_page_config(
    page_title = 'Streamlit Presentation',
    page_icon = '🍻'
)

a,b = st.columns(2)
st.title('What is MLflow?')

st.markdown('''
MLflow is an open source platform to manage the ML lifecycle, including experimentation, reproducibility, deployment, and a central model registry. MLflow currently offers four components:''')
buttons = []
for (i,j) in zip(st.columns(4),['MLflow Tracking','MLflow Projects','MLflow Models','Model Registry']):
    with i:
        #st.markdown(f"<p style='text-align: center; color: green; background-color:'>{j}</p>",unsafe_allow_html=True)
       buttons.append(st.button(j))
st.container()
if buttons[0]:
    st.info('''
 - The MLflow Tracking component is an API and UI for logging parameters, code versions, metrics, and output files when running your machine learning code and for later visualizing the results.
 - MLflow Tracking lets you log and query experiments using Python, REST, R, and Java API.

Storage:
1. Entity (Metadata) Store: for metrics, parameters, source, version
    * filesystem, SQL database, local or remote
2. Artifact Store: for data, models, plots etc.
    * local filesystem or remote stores like Amazon S3, Azure Blob, Google Cloud
    ''')
    st.image('mlflowtracking.png')
if buttons[1]: 
    st.info('''
 - Packaging format for reproducible runs on any platform
 - You can run the some code with the same results in any environment
 - Packaged code + config + dependencies + data = reproducible execution
 - Execution APIs and CLI (*mlflow run my_project*)
    ''')
    st.image('mlflowprojects.png')
if buttons[2]:
    st.info('''General model format that supports diverse deployment tools''')
    c1,c2 = st.columns(2)
    with c1:
        st.image('mlflowmodels1.png')
    
    with c2:
        st.image('mlflowmodels2.png')
        
    c1,c2 = st.columns(2)
    with c1:
       
        st.image('mlflowmodels3.png')
    with c2:
        
        st.image('mlflowmodels4.png')
if buttons[3]:
    st.info('''
- The MLflow Model Registry component is a centralized model store, set of APIs, and UI. 
- An MLflow Model can be registered with the Model Registry. A registered model has a unique name, contains versions, associated transitional stages, model lineage, and other metadata.
- After you have registered an MLflow model, you can serve the model as a service on your host.
''')


st.title('How to use MLflow?')


st.write('1. Start the MLflow tracking server. Or, by default, the MLflow Python API logs runs locally to files in an **mlruns** directory wherever you ran your program.  You can then run **mlflow ui** to see the logged runs.')
st.code('$ mlflow server --backend-store-uri sqlite:///mlflow.db --default-artifact-root ./artifacts --host 0.0.0.0 --port 5000')
st.write('''2. Record the training attempts during development (features, hyperparameters, performance metrics, the final trained model) locally or on the MLflow tracking server''')
st.code('''
mlflow.set_tracking_uri('http://localhost:5000')
mlflow.set_experiment('myproject_v2')

mlflow.start_run()
mlflow.log_param('features', feature_choice)
mlflow.log_metric('r2_score_train', r2_train)
mlflow.sklearn.log_model(model, 'mymodel')
mlflow.end_run()
''')

st.write('3. Register the final model in the Model Registry or save on your computer as an MLflow model')
st.code('''
mlflow.sklearn.save_model(model, 'my_model')
''')
st.write('4. Load the model from the local files or serve the final model as a service using the MLflow REST API')
st.code('''
$ mlflow models serve -m my_model --host 0.0.0.0 -p 5001 
''')
st.code('''
# Load the model from local files:
loaded_model = mlflow.sklearn.load_model(model_uri="models:/mymodel/Staging")
prediction = loaded_model.predict(test_data)

# Get the predictions from the MLflow REST API:     
import json
import requests     
ENDPOINT = "http://localhost:5001/invocations"

prediction = requests.post(
    url = ENDPOINT,
    data = test_data.to_json(orient='split'),
    headers={"Content-type": "application/json"}
    )
prediction = pd.DataFrame(json.loads(prediction.content.decode('utf-8')))
''')

st.image('mlflow_backend.png')

                 

