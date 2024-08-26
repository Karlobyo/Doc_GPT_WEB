import streamlit as st
import requests

'''
# Doc GPT

## Your personal medical assistant
#### Shed light onto complicated medical reports by summarizing their content to the essential
'''


with st.form(key='params_for_api'):


    question = st.text_input(label = "Please insert here the text from your document", value="")

    submit_button = st.form_submit_button('Summarize')


params = dict(question=question)



if submit_button:
    # Call the API
    api_url = 'http://127.0.0.1:8000/predict'
    response = requests.get(api_url, params=params)
    prediction = response.json()
    #pred = prediction['answer']

    '''
    Here is your summary:\n
    '''

    st.header(prediction)
