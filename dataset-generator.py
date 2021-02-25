import csv
import numpy as np

def phi(x, L, phi0, phiL, rho_eps):
    phi = -0.5 * rho_eps * np.power(x, 2) + ((phiL - phi0)/L + 0.5 * rho_eps * L) * x + phi0
    return phi

L = 1
dx = L / 100
x = np.arange(0, L, dx)
step = input("Unesite step: ")
step = int(step)
rho_eps = np.arange(-1000, 1001, step)

with open('dataset.csv', 'w') as csvfile:
    filewriter = csv.writer(
        csvfile, 
        delimiter=',',
        lineterminator='\n'
        )

    for step1 in range(-1000, 1001, 40):
        phi0 = step1
        for step2 in range(-1000, 1001, 40):
            phiL = step2
            for num in rho_eps:
                for _x in x:
                # print(num, phi(num))               
                    filewriter.writerow([_x, num, phi0, phiL, phi(_x, L, phi0, phiL, num)])