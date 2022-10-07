import streamlit as st

st.set_page_config(
    page_title = 'Streamlit Presentation',
    page_icon = '🍻'
)

a,b = st.columns(2)
st.title('What is MLflow?')

st.markdown('''
MLflow is an open source platform to manage the ML lifecycle, including experimentation, reproducibility, deployment, and a central model registry. MLflow currently offers four components:''')

for (i,j) in zip(st.columns(4),['MLflow Tracking','MLflow Projects','MLflow Models','Model Registry']):
    with i:
        st.markdown(f"<p style='text-align: center; color: green; background-color:'>{j}</p>",unsafe_allow_html=True)

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

                 

