import streamlit as st

from pyngrok import ngrok
from joblib import load

trained_model = load('model_sentiment.pkl')

form = st.form(key='my-form')

kalimat = form.text_input('Enter your sentence:')

submit = form.form_submit_button('Get the sentiment!')

if submit:
    y_pred = trained_model.predict([kalimat])
    st.write('The sentence has a sentiment: ', y_pred[0])

# ngrok_tunnel = ngrok.connect(8501)
# print('Public URL:', ngrok_tunnel.public_url)