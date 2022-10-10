import streamlit as st

st.set_page_config(
    page_title = 'Streamlit Presentation',
    page_icon = '🍻'
)


st.title('What is Flask?')
st.markdown('''
* Flask is a web framework written in Python
* We can serve our machine learning model on a Flask server 
''')
st.markdown('# How to use Flask?')
st.markdown('1. Develop the machine learning model and save it as a pickle file')
st.code('''
import pickle
with open('model.pkl','wb') as f:
   pickle.dump(model, f)
''')
st.markdown('2. Create the Flask app, load the model in the main script (app.py) and run the server')

with st.expander("app.py"):
    st.code('''
    from flask import Flask, request, jsonify
from flask import render_template
import pandas as pd
import pickle

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    json_ = request.get_json(force=True)
    query_df = pd.DataFrame(json_['data'])
    with open('model.pkl','rb') as f:
        model = pickle.load(f)
    prediction = model.predict(query_df)
    return jsonify({'prediction': list(prediction)})
''')

st.code('$ flask run --host 0.0.0.0 --port 8080')

st.markdown('3. Get the predictions from the Flask server to the Streamlit app with a POST request')

st.code('''
    import json
import requests
ENDPOINT = "http://localhost:8080/predict"
prediction = requests.post(
    url = ENDPOINT,
    data = test_data.to_json(orient='split'),
    headers={"Content-type": "application/json"}
    )
prediction = pd.DataFrame(json.loads(prediction.content.decode('utf-8')))
''')