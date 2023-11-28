from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array, load_img
import numpy as np
import tensorflow as tf
from keras.models import model_from_json
import cv2
import matplotlib.pyplot as plt

IMG_SIZE = (224, 224)

def load_model():
    # load json and create model
    json_file = open('model/best_model.json', 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = model_from_json(loaded_model_json)
    # load weights into new model
    loaded_model.load_weights("model/best_model.h5")
    return loaded_model


def get_image(path, img_size=IMG_SIZE):
    img = load_img(path, target_size=img_size)
    img = img_to_array(img) / 255.
    return img


def classify(path):
    model = load_model()
    label = ['clean', 'dirty']
    img = get_image(path, img_size=IMG_SIZE)
    my_image = img.reshape((1, img.shape[0], img.shape[1], img.shape[2]))
    y_pred = model.predict(my_image)
    y_hat = np.argmax(y_pr, axis=1)
    yi_hat = lbl[y_hat[0]]
    yi_pr = y_pr[0].max()
    title_sub = f"Prediction: {yi_hat} ({yi_pr:.1%})"
    print("\n")
    print(title_sub)
    return title_sub

