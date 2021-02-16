import os
from fastai.vision.all import *

SAVED_MODEL_PATH = './models/trained_model.pkl'
PATH_TO_TEST_IMAGES = './test_images/'

def _get_model():
    model = load_learner(SAVED_MODEL_PATH)
    return model

def get_list_of_images():
    file_list = os.listdir(PATH_TO_TEST_IMAGES)
    return [str(filename) for filename in file_list if str(filename).endswith('.png')]

def get_opened_image(image):
    return Image.open(image)

def perform_prediction(image_path):
    model = _get_model()
    pred = model.predict(PILImage.create(image_path))
    return pred[0]

