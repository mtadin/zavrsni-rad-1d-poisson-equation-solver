import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras import models

# dataset
dataset = pd.read_csv('dataset.csv', sep=',', names=['x', 'phi0', 'phiL', 'rho_eps', 'Labels'])
inputs = dataset.copy()

# normalizacija inputa
inputs['rho_eps'] = inputs['rho_eps']/1000
inputs['phi0'] = inputs['phi0']/1000
inputs['phiL'] = inputs['phiL']/1000

outputs = inputs.pop('Labels')
# print(inputs)
# print(outputs)

# model
model = keras.Sequential()
model.add(keras.layers.Dense(600, activation='relu'))
model.add(keras.layers.Dense(300, activation='relu'))
# model.add(keras.layers.Dense(150, activation='relu'))
# model.add(keras.layers.Dense(25, activation='relu'))
model.add(keras.layers.Dense(1))
adam = tf.keras.optimizers.Adam(epsilon=1.0)
model.compile(loss='mse', optimizer=adam)

# treniranje modela
model.fit(inputs.values, outputs.values, batch_size=100, epochs=100)

# spremanje modela
modelName = input("Unesite ime modela za spremanje: ")
model.save('./models/' + modelName + '.h5')
print('Model spremljen kao ' + modelName + '.h5')