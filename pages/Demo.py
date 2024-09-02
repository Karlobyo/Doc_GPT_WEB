import streamlit as st
import requests

import cv2 as cv
import numpy as np


from bg_loader import add_bg_from_local


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

#with st.form(key='params_for_summary_api'):

text = ""

options = ["Anxiety patient", "Diabetes patient"]

selected_option = st.selectbox(label="Choose an option:", options=options, index=None)
if selected_option:
    if selected_option == "Anxiety patient":
        text = """Original text:\n
        Jim is a 56-year-old male. He is currently diagnosed with Major Depressive Disorder and
        Anxiety Disorder and has been experiencing symptoms for many years. Jim presents well,
        appearing well-spoken. However, upon delving deeper into his history and symptoms, he
        experiences a significant amount of anxiety, tension, and paranoia surrounding his day-to-day
        life. He has difficulties in social situations, especially meeting new people, being in crowded
        areas, or tolerating social situations. He often picks at his hands when relaying symptoms and is
        in pain daily. He experiences significant symptoms of depression as well that debilitate him to
        the point of being unable to leave his house or tent. He is easily agitated and quick to become
        angry. He feels that his mood shifts quickly where one moment he is functional and the next he
        can't leave the house or tent. He is always on edge, and when feeling depressed, can't move and
        it's hard to even get out of bed. He feels shaky and unsteady as he isolates from others."""



    else:

        text = """Original text:\n
        A 14-year-old girl was admitted to our pediatric ward for a second opinion after 2-year history of CDI.
        The blood tests at the time of first evaluation revealed hypernatremia (Na 147 mEq/L), high plasma osmolality (POsm; 305 mOsm/kg/H2O),
        yet low urine osmolality (UOsm; 109 mOsm/Kg/ H2O) that led to the diagnosis of CDI
        for which the girl was treated with desmopressin. Sixteen months later,
        decrease of water intake and urine output was observed, although no recent variation of
        body weight or desmopressin dose had been reported. Due to the improvement of polyuria,
        her physician reduced desmopressin dose progressively, until normalization of water output
        was reported 2 months later. This led to a diagnosis of reversible CDI, and desmopressin
        treatment was therefore withdrawn. Two months later (18 months since first diagnosis),
        she experienced extreme fatigue, nausea, progressive memory loss up to confusion,
        and lethargy. Patient's mother contacted our center, and the girl was first seen at our
        department 24 months after the diagnosis of CDI. Clinical examination revealed signs of
        dehydration, behavior and sensory disturbances, and confusion, while laboratory analyses
        revealed hypernatremia (Na 156 mEq/L), high POsm (330 mOsm/kg/H2O), low UOsm (84 mOsm/Kg/ H2O),
        low morning cortisol (80 nmol/L n.v. 138-635 nmol/L), and adrenocorticotropic hormone levels (0.88 pmol/L, n.v.1.3-16.7 pmol/L)
        as well as low thyrotropin (0.1 mU/L, n.v. 0.4-4 mU/L) and thyroxine values
        (0.68 ng/dL; n.v. 0.7-1.9 ng/dL).
        """

    st.markdown(text)

#if selected_option:
submit_button = st.button('Summarize')


min_length = 20
max_length = 30
params_sum = dict(text=text, min_length=min_length, max_length=max_length)


if submit_button:
    # Call the API
    api_url = 'http://127.0.0.1:8000/summarize'
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



#with st.form(key='params_for_doc_api'):

doc = ""
question = ""

patients = ["Anxiety patient", "Schizofrenia patient"]

selected_doc = st.selectbox(label="Choose a document:",
                                options=patients, index=None)


if selected_doc:
    if selected_doc == "Anxiety patient":
        doc = """Original text:\n
        Jim is a 56-year-old male. He is currently diagnosed with Major Depressive Disorder and
        Anxiety Disorder and has been experiencing symptoms for many years. Jim presents well,
        appearing well-spoken. However, upon delving deeper into his history and symptoms, he
        experiences a significant amount of anxiety, tension, and paranoia surrounding his day-to-day
        life. He has difficulties in social situations, especially meeting new people, being in crowded
        areas, or tolerating social situations. He often picks at his hands when relaying symptoms and is
        in pain daily. He experiences significant symptoms of depression as well that debilitate him to
        the point of being unable to leave his house or tent. He is easily agitated and quick to become
        angry. He feels that his mood shifts quickly where one moment he is functional and the next he
        can't leave the house or tent. He is always on edge, and when feeling depressed, can't move and
        it's hard to even get out of bed. He feels shaky and unsteady as he isolates from others."""



    else:

        doc = """Original text:\n
        A 14-year-old girl was admitted to our pediatric ward for a second opinion after 2-year history of CDI.
        The blood tests at the time of first evaluation revealed hypernatremia (Na 147 mEq/L), high plasma osmolality (POsm; 305 mOsm/kg/H2O),
        yet low urine osmolality (UOsm; 109 mOsm/Kg/ H2O) that led to the diagnosis of CDI
        for which the girl was treated with desmopressin. Sixteen months later,
        decrease of water intake and urine output was observed, although no recent variation of
        body weight or desmopressin dose had been reported. Due to the improvement of polyuria,
        her physician reduced desmopressin dose progressively, until normalization of water output
        was reported 2 months later. This led to a diagnosis of reversible CDI, and desmopressin
        treatment was therefore withdrawn. Two months later (18 months since first diagnosis),
        she experienced extreme fatigue, nausea, progressive memory loss up to confusion,
        and lethargy. Patient's mother contacted our center, and the girl was first seen at our
        department 24 months after the diagnosis of CDI. Clinical examination revealed signs of
        dehydration, behavior and sensory disturbances, and confusion, while laboratory analyses
        revealed hypernatremia (Na 156 mEq/L), high POsm (330 mOsm/kg/H2O), low UOsm (84 mOsm/Kg/ H2O),
        low morning cortisol (80 nmol/L n.v. 138-635 nmol/L), and adrenocorticotropic hormone levels (0.88 pmol/L, n.v.1.3-16.7 pmol/L)
        as well as low thyrotropin (0.1 mU/L, n.v. 0.4-4 mU/L) and thyroxine values
        (0.68 ng/dL; n.v. 0.7-1.9 ng/dL).
        """

    st.markdown(doc)

    if selected_doc == patients[0]:

        questions = ["What does Jim suffer from?", "What are the effects of this disease?"]

        selected_question = st.selectbox(label="Choose a question:",
                                options=questions, index=None)


        if selected_question == questions[0]:
            question = "What does Jim suffer from?"
        else:
            question = "What are the effects of this disease?"


    else:

        questions = ["What treatment is recommended?", "How were the blood tests?"]

        selected_question = st.selectbox(label="Choose a question:",
                                options=questions, index=None)


        if selected_question == "What treatment is recommended?":
            question = "What treatment is recommended?"
        else:
            question = "How were the blood tests?"

    if selected_doc is not None and selected_question is not None:
        submit_button = st.button('Ask')


# min_length = 20
# max_length = 100
params_doc = dict(doc=doc,
              question=question)#, min_length=min_length, max_length=max_length)



if submit_button:
    # Call the API
    api_url = 'http://127.0.0.1:8000/document'
    response = requests.get(api_url, params=params_doc)
    prediction = response.json()

    # st.markdown(
    #     "<p style='color:black;'>Here is the answer:</p>",
    #     unsafe_allow_html=True
    # )

    st.header(prediction)

st.markdown('***')

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
    api_url = 'http://127.0.0.1:8000/document_upload'
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
