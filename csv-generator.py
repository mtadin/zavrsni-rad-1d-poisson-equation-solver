import csv
import numpy as np

def phi(x, L, phi0, phiL, rho_eps):
    phi = -0.5 * rho_eps * np.power(x, 2) + ((phiL - phi0)/L + 0.5 * rho_eps * L) * x + phi0
    return phi

phi0 = 100
phiL = 0
L = 1
dx = L / 100
x = np.arange(0, L, dx)
rho_eps = np.arange(-1000, 1001, 10)

with open('dataset.csv', 'w') as csvfile:
    filewriter = csv.writer(
        csvfile, 
        delimiter=',',
        lineterminator='\n'
        )

    for num in rho_eps:
        for _x in x:
        # print(num, phi(num))               
            filewriter.writerow([_x, num, phi(_x, L, phi0, phiL, num)])