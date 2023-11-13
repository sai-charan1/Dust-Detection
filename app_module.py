import tensorflow as tf
from tensorflow.keras.models import load_model
import os

BEST_MODEL_PATH = os.path.join(os.getcwd(), 'vgg16_tl_ft_solar_dust.h5')

best_model = load_model(BEST_MODEL_PATH)
best_model.summary()

