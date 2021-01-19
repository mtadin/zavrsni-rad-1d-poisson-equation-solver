import numpy as np
import pandas as pd

phi0 = 100
phiL = 0
L = 10
dx = L / 100
x = np.arange(0, L, dx)
rho_eps = 50
phi = -0.5 * rho_eps * np.power(x, 2) + ((phiL - phi0)/L + 0.5 * rho_eps * L) * x + phi0

print(phi)

dataset = pd.read_csv('dataset.csv')
print(dataset)

# generator koji sluzi kao podaci za treniranje modela
# num predstavlja ro_eps varijablu
# def dataset_generator(step =50, lower =-1000, upper =1000):
#     num = lower
#     while num <= upper:
#         yield (num, phi(num))
#         num += step

# np.arange(start, stop, step) -> 1:3:10 u matlabu = arange(1,11,3) u pythonu
# rho_eps = np.arange(-1000, 1001, 50)

# drugi model
# model = keras.Sequential()
# model.add(keras.layers.Dense(10, input_shape=(1,)))
# model.add(keras.layers.Activation('relu'))
# model.add(keras.layers.Dense(20) )
# model.add(keras.layers.Activation('relu'))
# model.add(keras.layers.Dense(1))
# model.compile(loss='mse', optimizer='adam')

#sklearn preprocessing min/max scaler