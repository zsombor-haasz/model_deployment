import streamlit as st

st.set_page_config(
    page_title = 'Streamlit Presentation',
    page_icon = '🍻'
)

st.title('BentoML')

st.markdown('''
Steps:
1. Train the  machine learning model
2. Save the model to BentoML local store
''')
st.code("import bentoml\nbento_model = bentoml.sklearn.save_model('model',model)")
st.code('$ bentoml models list')
st.markdown('3. Create a BentoML service')

st.code('''
import bentoml
from bentoml.io import NumpyNdarray
import numpy as np

BENTO_MODEL_TAG = 'model:x5pov5saw2ih4kar'

# the Runner: a wrapper around the model
model_runner =  bentoml.sklearn.get(BENTO_MODEL_TAG).to_runner()
# the Service
sklearn_service = bentoml.Service('my_regression', runners = [model_runner])
#the API
@sklearn_service.api(input=NumpyNdarray(), output=NumpyNdarray())
def classify(input_data: np.array) -> np.array:
    return model_runner.predict.run(input_data)
''')
st.markdown('You can run the bentoml service and get the predictions through a POST request:')
st.code('$ bentoml serve bento_app:sklearn_service --reload')
st.code('''
import numpy as np
import json
import requests
ENDPOINT = 'http://localhost:3000/predict'
prediction = requests.post(
    ENDPOINT,
    headers={"content-type": "application/json"},
    data=json.dumps(np.asarray(test_data).tolist())
    )
prediction = pd.DataFrame(json.loads(prediction.content.decode('utf-8')))      
''')
st.markdown('4. Build a **bento**. A bento is the unit of deployment: it has both the model and the service in a single entity. First, you have to create a yaml configuration file.')
st.code('''
$ bentoml build
$ bentoml list''')
st.markdown('5. Serve the model  through a *bento*')
st.code('$ bentoml serve my_regression:2oo4drkayw5lakar --production')
st.markdown('6. Dockerise the *bento*')
st.code('$ bentoml containerize my_regression:2oo4drkayw5lakar')
st.markdown('7. Run bento service via Docker') 
st.code('$ docker run -p 3000:3000 my_regression:2oo4drkayw')
st.markdown('''
8. Deployment options: https://docs.bentoml.org/en/latest/concepts/deploy.html
* Kubernetes: yatai
* Cloud platforms: bentoctl
''')


