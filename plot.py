import numpy as np
import pandas as pd
from tensorflow.keras.models import load_model
import matplotlib.pyplot as plt
import csv

# uzimanje korisnikovog unosa
while True:
    try:
        inputNumber = int(input("> Unesite broj koji zelite isprobati: "))
        break
    except:
        print("> Unesite integer!")

modelName = input("> Unesite naziv modela kojim zelite vrsiti usporedbu: ")
modelName = modelName + '.h5'

phi0 = 100
phiL = 0

x = np.arange(0, 1, 0.01)
# stvaranje filea za usporedbu
with open('test.csv', 'w') as csvfile:
    filewriter = csv.writer(
        csvfile, 
        delimiter=',',
        lineterminator='\n'
        )

    for _x in x:             
        filewriter.writerow([_x, phi0, phiL, inputNumber])

# ucitavanje spremljenog modela
try:
    if modelName != '.h5':
        model = load_model('./models/' + modelName)
    else:
        model = load_model('./models/e60s10.h5')
except:
    print("> Model ne postoji!")

# usporedba grafova
test = pd.read_csv('test.csv', sep=',', names=['x', 'phi0', 'phiL', 'y'])

# normalizacija inputa
test['y'] = test['y']/1000
test['phi0'] = test['phi0']/1000
test['phiL'] = test['phiL']/1000

predictNew = model.predict(test)

def phi(x, L, phi0, phiL, rho_eps):
    phi = -0.5 * rho_eps * np.power(x, 2) + ((phiL - phi0)/L + 0.5 * rho_eps * L) * x + phi0
    return phi

L = 1
dx = L / 100
x = np.arange(0, L, dx)
rho_eps = inputNumber

plt.plot(x, phi(x, L, phi0, phiL, rho_eps))
plt.plot(x, predictNew)
plt.legend(["Analiticko rjesenje", "Generirano rjesenje"])
plt.show()