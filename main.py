import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras import models
# import matplotlib.pyplot as plt

# dataset
dataset = pd.read_csv('dataset.csv', sep=',', names=['x', 'rho_eps', 'Labels'])
inputs = dataset.copy()
inputs['rho_eps'] = inputs['rho_eps']/1000
outputs = inputs.pop('Labels')
print(inputs)
print(outputs)

# model
model = keras.Sequential()
model.add(keras.layers.Dense(30, activation='relu'))
model.add(keras.layers.Dense(1))
model.compile(loss='mse', optimizer='adam') # optimizer SGD ili adam

# treniranje modela
model.fit(inputs.values, outputs.values, epochs=100)

# predictions
predictions = model.predict(inputs.values)
print(predictions[:5, :])
print(outputs.values[:5])