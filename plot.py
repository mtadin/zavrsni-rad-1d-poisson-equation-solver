import numpy as np
import pandas as pd
from tensorflow.keras.models import load_model
import matplotlib.pyplot as plt

# dataset
dataset = pd.read_csv('dataset.csv', sep=',', names=['x', 'rho_eps', 'Labels'])
inputs = dataset.copy()
inputs['rho_eps'] = inputs['rho_eps']/1000 # normalizacija inputa
outputs = inputs.pop('Labels')
# print(inputs)
# print(outputs)

# ucitavanje spremljenog modela
model = load_model('model_example.h5')

# predictions
predictions = model.predict(inputs.values)

print(predictions[:5, :])
print(outputs.values[:5])

# prikaz grafova
x = np.arange(0, 1, 0.01)
plt.plot(x, outputs.values[:100])
plt.plot(x, predictions[:100, :])
plt.legend(["Analiticko rjesenje", "Generirano rjesenje"])
plt.show()

plt.plot(x, outputs.values[10000:10100])
plt.plot(x, predictions[10000:10100, :])
plt.legend(["Analiticko rjesenje", "Generirano rjesenje"])
plt.show()

plt.plot(x, outputs.values[20000:20100])
plt.plot(x, predictions[20000:20100, :])
plt.legend(["Analiticko rjesenje", "Generirano rjesenje"])
plt.show()