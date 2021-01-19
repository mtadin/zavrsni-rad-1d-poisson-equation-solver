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
inputs['rho_eps'] = inputs['rho_eps']/1000 # normalizacija inputa
outputs = inputs.pop('Labels')
print(inputs)
print(outputs)

# model
model = keras.Sequential()
model.add(keras.layers.Dense(200, activation='relu'))
model.add(keras.layers.Dense(100, activation='relu'))
# model.add(keras.layers.Dense(10, activation='relu')) treci sloj usporava treniranje, a opcenito ne poboljsava rezultate
model.add(keras.layers.Dense(1))
adam = tf.keras.optimizers.Adam(epsilon=1.0) # default value: 1e-7
# prema zabiljesci u api dokumentaciji za adam optimizer, default vrijednost nije primjenjiva u svim slucajevima
# postavljena na 0.1 daje opcenito jednake rezultate u 50 epoha manje
# postavljena na 1.0 daje visestruko manje rezultate u 50 epoha manje
model.compile(loss='mse', optimizer=adam) # optimizer SGD ili adam

# treniranje modela
model.fit(inputs.values, outputs.values, epochs=60)

# predictions
predictions = model.predict(inputs.values)
print(predictions[:5, :])
print(outputs.values[:5])