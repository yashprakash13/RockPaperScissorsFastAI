import os
import sys

sys.path.append('models')
sys.path.append('modules')

import streamlit as st

from load_model import *


st.sidebar.title("RPS Image Classifier")

PATH_TO_TEST_IMAGES = './test_images/'


def classify(image_file):
    pred = perform_prediction(image_file)
    return pred
    


def main():
    st.sidebar.subheader('Load image')
    image_file_uploaded = st.sidebar.file_uploader('Upload an image', type = 'png')
    st.sidebar.text('OR')
    image_file_chosen = st.sidebar.selectbox('Select an existing image:', get_list_of_images())
    
    image_file = None
    if image_file_uploaded:
        image_file = image_file_uploaded
    elif image_file_uploaded and image_file_chosen:
        image_file = image_file_uploaded
    else:
        image_file = image_file_chosen


    if image_file_uploaded and image_file and st.sidebar.button('Load'):
        image = get_opened_image(image_file)
        with st.beta_expander('Selected Image', expanded = True):
            st.image(image, use_column_width = True)
    
    if image_file_chosen and image_file and st.sidebar.button('Load'):
        image = get_opened_image(os.path.join(PATH_TO_TEST_IMAGES, image_file))
        with st.beta_expander('Selected Image', expanded = True):
            st.image(image, use_column_width = True)
    
        
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        
        prediction = classify(os.path.join(PATH_TO_TEST_IMAGES, image_file))
        st.subheader('Prediction') 
        st.markdown(f'The predicted label is: **{prediction}**')

        


main()


