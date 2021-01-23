import glob
import numpy as np
import pandas as pd
from tensorflow.keras.models import load_model
import matplotlib.pyplot as plt
import csv

files = glob.glob('models/*.h5')
print('> Detektirano ' + str(len(files)) + ' modela.')

# uzimanje korisnikovog unosa
while True:
    try:
        comparisonNumber = int(input("> Unesite broj koji zelite isprobati: "))
        break
    except:
        print("> Unesite integer!")

x = np.arange(0, 1, 0.01)
# stvaranje filea za usporedbu
with open('comparison.csv', 'w') as csvfile:
    filewriter = csv.writer(
        csvfile, 
        delimiter=',',
        lineterminator='\n'
        )

    for _x in x:             
        filewriter.writerow([_x, comparisonNumber])

for f in files:
    model = load_model(f)
    comparison = pd.read_csv('comparison.csv', sep=',', names=['x', 'y'])
    comparison['y'] = comparison['y']/1000 # normalizacija inputa

    predictNew = model.predict(comparison)

    def phi(x, L, phi0, phiL, rho_eps):
        phi = -0.5 * rho_eps * np.power(x, 2) + ((phiL - phi0)/L + 0.5 * rho_eps * L) * x + phi0
        return phi

    phi0 = 100
    phiL = 0
    L = 1
    dx = L / 100
    x = np.arange(0, L, dx)
    rho_eps = comparisonNumber

    # TODO load all plots in one figure
    plt.title(f)
    plt.plot(x, phi(x, L, phi0, phiL, rho_eps))
    plt.plot(x, predictNew)
    plt.legend(["Analiticko rjesenje", "Generirano rjesenje"])
    plt.show()