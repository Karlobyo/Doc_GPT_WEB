import streamlit as st
import requests
import base64

def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"jpg"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )


st.set_page_config(layout='wide')

# Add custom CSS to change the text color to black in the headers

CSS = """
h1 {
    color: black;
}
h2 {color: black;
}
h3 {color: black;
}
h4 {color: black;
}
.stApp {
    background-image: webinterface/app_cloud.py;
    background-size: cover;
"""
st.write(f'<style>{CSS}</style>', unsafe_allow_html=True)

add_bg_from_local('pics/medical-pic.jpg')


'''
# Doc GPT

## Your personal medical assistant
### Shed light onto complicated medical reports by summarizing their content to the essential
'''

# Add custom CSS to change the text color to black in the markdowns
st.markdown(
    """
    <style>
    label {
        color: black !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)


with st.form(key='params_for_api'):


    question = st.text_input(label = "Please insert here the text from your document",
                             value="")

    submit_button = st.form_submit_button('Summarize')


params_sum = dict(question=question)




if submit_button:
    # Call the API
    api_url = 'http://127.0.0.1:8000/summarize'
    response = requests.get(api_url, params=params_sum)
    prediction = response.json()

    st.markdown(
        "<p style='color:black;'>Here is your summary:</p>",
        unsafe_allow_html=True
    )

    st.header(prediction)




with st.form(key='params_for_api'):


    doc_url = st.text_input(label = "Please insert here the document URL",
                             value="")

    question = st.text_input(label = "Please insert here your question",
                             value="")

    submit_button = st.form_submit_button('Ask')


params_doc = dict(doc_url=doc_url,
              question=question)




if submit_button:
    # Call the API
    api_url = 'http://127.0.0.1:8000/document'
    response = requests.get(api_url, params=params_doc)
    prediction = response.json()

    st.markdown(
        "<p style='color:black;'>Here is the answer:</p>",
        unsafe_allow_html=True
    )

    st.header(prediction)
