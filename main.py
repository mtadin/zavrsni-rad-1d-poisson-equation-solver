import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras import models
# import matplotlib.pyplot as plt

# dataset
dataset = pd.read_csv('dataset.csv', sep=',', names=['Features', 'Labels'])
inputs = dataset.copy()
outputs = inputs.pop('Labels')

# model
model = keras.Sequential()
model.add(keras.layers.Dense(1, input_shape=(1,2)))
model.compile(loss='mse', optimizer='SGD') # optimizer SGD ili Adadelta

# treniranje modela
model.fit(inputs, outputs)

# predictions
# predictions = model.predict()
# print(predictions)