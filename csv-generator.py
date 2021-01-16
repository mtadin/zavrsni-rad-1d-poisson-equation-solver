import csv
import numpy as np

def phi(rho_eps):
    phi0 = 100
    phiL = 0
    L = 10
    dx = L / 100
    x = np.arange(0, L, dx)
    phi = -0.5 * rho_eps * np.power(x, 2) + ((phiL - phi0)/L + 0.5 * rho_eps * L) * x + phi0
    return phi.tolist() # tolist uklanja newline charactere iz numpy arraya

rho_eps = np.arange(-1000, 1001, 50)

with open('dataset.csv', 'w') as csvfile:
    filewriter = csv.writer(
        csvfile, 
        delimiter=',',
        )

    for num in rho_eps:
        # print(num, phi(num))               
        filewriter.writerow([num, phi(num)])