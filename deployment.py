import streamlit as st
import requests
from streamlit_lottie import st_lottie
import joblib
import numpy as np
from PIL import Image
st.set_page_config(page_title='Fake News Detetector', page_icon='::star::')
loaded_model = joblib.load(open("model_detection_HHH", 'rb'))
image = Image.open('logo.png')

def load_lottie(url): # test url if you want to use your own lottie file 'valid url' or 'invalid url'
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()





nav=st.sidebar.radio('', ["Home","About"])
if nav == "Home":

   
    lottie_link = "https://assets4.lottiefiles.com/packages/lf20_yb7fmrm7.json"
    animation = load_lottie(lottie_link)
    lottie_link2 = "https://assets6.lottiefiles.com/packages/lf20_aXM2jEiatF.json"
    animation2 = load_lottie(lottie_link2)
    
    col1, col2 = st.columns([1, 3])
    with col1:
    #st.image(image, caption='Powered by')
        st_lottie(animation2, speed=1, height=150)
    with col2:
     
        st.markdown("<h1 style='text-align: center; color: black;'>Fake News Detetector</h1>", unsafe_allow_html=True)


    st.write('---')

    st.subheader('Your suspicious News goes here')

    txt = st.text_area('')
    txt=[txt]

    if st.button('Reveal!'):
           pred_Y = loaded_model.predict(txt)
           label=str(pred_Y) 
           if label=="['Fake']":
                st.subheader("FAKE NEWS")
                
           else:
            st.subheader("REAL NEWS")
                
                
           #label.replace('[', ' ')
           #label.replace(']', ' ')
           #label.translate({ord('b'): None})
           #st.subheader(label)
    st_lottie(animation, speed=1, height=300, key="initial")


if nav == "About":
        lottie_link3 = "https://assets5.lottiefiles.com/packages/lf20_ljotbiif.json"
        animation3 = load_lottie(lottie_link3)
        lottie_link4 ="https://assets8.lottiefiles.com/packages/lf20_iotglorw.json"
        animation4 = load_lottie(lottie_link4)

        col1, col2 = st.columns(2)
        with col1:
           #st.subheader("This Detector was made by machine learning concepts and Trained on large data set of news from various sources")
           #st.subheader("techincal concepts :")
           #st.write("1 - Natural Language Processing (NLP)")
           #st.write("2 - text vectorizer: TFIDF")
           #st.write("3 - classification models:")
           #st.write("Logistic regression , SVM ")
           st.markdown("<font style='text-align: left; color: black;font-size:170%;font-weight:Bold'>Here's Our Detector's Details</font>", unsafe_allow_html=True)
           st.markdown("<font style='text-align: left; color: black;font-size:130%;font-weight:Bold'>Techincal concepts :</font>", unsafe_allow_html=True)
           st.markdown("<font style='text-align: left; color: black;font-size:130%;font-weight:Semi Bold'>1- Natural Language Processing (NLP)</font>", unsafe_allow_html=True)
           st.markdown("<font style='text-align: left; color: black;font-size:130%;'>2- Text vectorizer: TFIDF</font>", unsafe_allow_html=True)
           st.markdown("<font style='text-align: left; color: black;font-size:130%;'>3- Classification models  </font>", unsafe_allow_html=True)
           st.markdown("<font style='text-align: left; color: black;font-size:130%;'>4- Logistic regression , SVM </font>", unsafe_allow_html=True)
        with col2:
           st_lottie(animation3, speed=1.5, height=450) 


        col1, col2 = st.columns(2)
        with col1:   
         #st.header("Credits : ")
         st.markdown("<font style='text-align: left; color: black;font-size:160%;font-weight:Bold'>Credits</font>", unsafe_allow_html=True)
         st.markdown("<font style='text-align: left; color: black;font-size:120%;'>[Hesham Yehia](https://www.linkedin.com/in/hesham-yehia/)</font>", unsafe_allow_html=True)
         st.markdown("<font style='text-align: left; color: black;font-size:120%;'>[Ammar Thabet](https://www.linkedin.com/in/ammar-thabett/)</font>", unsafe_allow_html=True)
         st.markdown("<font style='text-align: left; color: black;font-size:120%;'>[Ahmed Sameh](https://www.linkedin.com/in/ahmedsamehahmed/)</font>", unsafe_allow_html=True)
         
        # st.subheader("[Hesham Yehia](https://www.linkedin.com/in/hesham-yehia/)")
        #st.subheader("[Ammar Thabet](https://www.linkedin.com/in/ammar-thabett/)")
        # st.subheader("[Ahmed Sameh](https://www.linkedin.com/in/ahmedsamehahmed/)")
         with col2:
             #st_lottie(animation4, speed=1.5, height=370)
              st.image(image, caption='Powered by')
        #st.subheader("Hesham Yehia")
        #st.subheader("Ammar Thabet")
        #st.subheader("Ahmed Sameh")

  






