import streamlit as st
import requests

import cv2 as cv
import numpy as np


from bg_loader import add_bg_from_local


URL = "http://127.0.0.1:8000"
#URL = "https://docgpt-72mal6ptca-ew.a.run.app"


st.set_page_config(layout='wide')

# Add custom CSS to change the text color to black in the headers

# CSS = """
# h1 {
#     color: black;
# }
# h2 {color: black;
# }
# h3 {color: black;
# }
# h4 {color: black;
# }
# .stApp {
#     background-image: webinterface/app_cloud.py;
#     background-size: cover;
# """
# st.write(f'<style>{CSS}</style>', unsafe_allow_html=True)

# add_bg_from_local('pics/medical-pic.jpg')


'''
# Doc GPT

## Your personal medical assistant
#### *Shed light onto complicated medical reports*

***

'''

# Add custom CSS to change the text color to black in the markdowns
# st.markdown(
#     """
#     <style>
#     label {
#         color: black !important;
#     }
#     </style>
#     """,
#     unsafe_allow_html=True
# )

'''
### Summarize
'''

with st.form(key='params_for_summary_api'):


    text = st.text_input(label = "Please insert here the text from your document",
                             value="")

    submit_button = st.form_submit_button('Summarize')


params_sum = dict(text=text)




if submit_button:
    # Call the API
    api_url = f'{URL}/summarize'
    response = requests.get(api_url, params=params_sum)
    prediction = response.json()

    # st.markdown(
    #     "<p style='color:black;'>Here is your summary:</p>",
    #     unsafe_allow_html=True
    # )

    st.header(prediction)

'''
***
'''


'''
### Ask questions
'''


with st.form(key='params_for_doc_api'):


    doc = st.text_input(label = "Please insert here the text from your document",
                             value="")


    question = st.text_input(label = "Please insert here your question",
                             value="")

    submit_button = st.form_submit_button('Ask')


params_doc = dict(doc=doc,
              question=question)



if submit_button:
    # Call the API
    api_url = f'{URL}/document'
    response = requests.get(api_url, params=params_doc)
    prediction = response.json()

    # st.markdown(
    #     "<p style='color:black;'>Here is the answer:</p>",
    #     unsafe_allow_html=True
    # )

    st.header(prediction)



st.markdown('Or upload an image (jpg, jpeg, png, bmp) of your document:')

uploaded_file = st.file_uploader("", type=["jpg", "jpeg", "png", "bmp"])

image_u=None

save_path=None

if uploaded_file is not None:

    # decode
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    image_u = cv.imdecode(file_bytes, cv.IMREAD_COLOR)

    #save_path = f"Doc_GPT_WEB/docs/uploaded_docs/{uploaded_file}.png"

    save_path = "docs/receipt.png"


    #cv.imwrite(save_path, image_u)

    # display uploaded image
    st.image(image_u, width=800, channels="BGR", caption='uploaded image')


with st.form(key='params_for_doc_2_api'):

    image_path = "/Users/carlobarbini/code/Karlobyo/doc_gpt_project/Doc_GPT_WEB/docs/list_app.png"

    question = st.text_input(label = "Please insert here your question",
                             value="")

    submit_button = st.form_submit_button('Ask')


params_doc_2 = dict(image_path=image_path,
                  question=question)


if submit_button:
    # Call the API
    api_url = f'{URL}/document_upload'
    response = requests.get(api_url, params=params_doc_2)

    if response.status_code == 200:

        prediction = response.json()

        # st.markdown(
        #     "<p style='color:black;'>Here is the answer:</p>",
        #     unsafe_allow_html=True
        # )

        st.header(prediction)

    else:

        st.markdown("Please use a valid document format >> jpeg, jpg, png, bmp")














# st.markdown('Or upload an image from your browser:')

# uploaded_file = st.file_uploader("", type=["jpg", "jpeg", "png", "bmp"])

# image_u = None

# if uploaded_file is not None:
#     # Read and decode the uploaded file
#     file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
#     image_u = cv.imdecode(file_bytes, cv.IMREAD_COLOR)

#     # Display uploaded image
#     st.image(image_u, width=200, channels="BGR", caption='Uploaded image')

# with st.form(key='params_for_doc_2_api'):
#     question = st.text_input(label="Please insert your question here", value="")
#     submit_button = st.form_submit_button('Ask')

# if submit_button and uploaded_file is not None:
#     # Re-read the uploaded file for sending as binary
#     uploaded_file.seek(0)  # Reset file pointer to the start
#     image_data = uploaded_file.read()

#     # Prepare the payload for the request
#     params_doc_2 = {
#         "question": question
#     }

#     # Send POST request to the API with the image file
#     api_url = 'http://127.0.0.1:8000/document_2'
#     files = {'image': image_data}

#     response = requests.post(api_url, files=files, data=params_doc_2)

#     if response.status_code == 200:
#         prediction = response.json()

#         st.markdown(
#             "<p style='color:black;'>Here is the answer:</p>",
#             unsafe_allow_html=True
#         )
#         st.header(prediction)#.get('answer', 'No answer found.'))
#     else:
#         st.error(f"Error: {response.status_code} - {response.text}")

# else:
#     if submit_button and uploaded_file is None:
#         st.warning("Please upload an image first.")
