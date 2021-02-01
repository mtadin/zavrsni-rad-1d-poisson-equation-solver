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
model.add(keras.layers.Dense(200, activation='relu'))
model.add(keras.layers.Dense(100, activation='relu'))
# model.add(keras.layers.Dense(10, activation='relu')) treci sloj usporava treniranje, a opcenito ne poboljsava rezultate
model.add(keras.layers.Dense(1))
adam = tf.keras.optimizers.Adam(epsilon=1.0) # default value: 1e-7 
# epsilon predstavlja konstantu za numericku stabilnost u metodi stohastickog gradijentnog spusta
# prema zabiljesci u api dokumentaciji za adam optimizer, default vrijednost nije primjenjiva u svim slucajevima
# postavljena na 0.1 daje opcenito jednake rezultate u 50 epoha manje
# postavljena na 1.0 daje visestruko bolje rezultate u 50 epoha manje
model.compile(loss='mse', optimizer=adam) # optimizer adam ili SGD

# treniranje modela
model.fit(inputs.values, outputs.values, epochs=250)

# spremanje modela
modelName = input("Unesite ime modela za spremanje: ")
model.save('./models/' + modelName + '.h5')
print('Model spremljen kao ' + modelName + '.h5')