import streamlit as st
import numpy as np
from tensorflow.keras.models import model_from_json
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.imagenet_utils import preprocess_input

# Load the model architecture from JSON
with open('D:/Projects/solar-panel-dust-detection/Dust-Detection/model/best_model.json', 'r') as json_file:
    model_json = json_file.read()

# Convert JSON string to model
model = model_from_json(model_json)

# Load the model weights
model.load_weights('D:/Projects/solar-panel-dust-detection/Dust-Detection/model/best_model.h5')

# Streamlit UI
st.title("Solar Panel Dust Detection")

# Upload image
uploaded_file = st.file_uploader("Choose an image...", type="jpg")

if uploaded_file is not None:
    # Display image
    img = image.load_img(uploaded_file, target_size=(224, 224))
    st.image(img, caption='Uploaded Image', use_column_width=True)
    st.write("")
    
    # Preprocess image
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = preprocess_input(img_array)

    # Predict
    prediction = model.predict(img_array)
    
    # Display prediction result
    st.write("Prediction:", prediction)
