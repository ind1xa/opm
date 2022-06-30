import numpy as np
import matplotlib.pyplot as plt

M = 1000            #h = 0.001

prviRedGM = [2*M, -M]
zadnjiRedGM = []

for i in range(M-2):
    prviRedGM.append(0)
    zadnjiRedGM.append(0)

zadnjiRedGM.append(-M)
zadnjiRedGM.append(2*M)

globalnaMatrica = []
globalnaMatrica.append(prviRedGM)

for i in range(M-2):
    redGM = []
    for j in range(M):
        if i == j:
            redGM.append(-M)
        elif i == j-1:
            redGM.append(2*M)
        elif i == j-2:
            redGM.append(-M)
        else:
            redGM.append(0)
    globalnaMatrica.append(redGM)

globalnaMatrica.append(zadnjiRedGM)

#print(globalnaMatrica)

vektorDesneStrane = []

for i in range(0, M):
    vektorDesneStrane.append((1+i/M)/M)        #Ax = f * h**2    , h = 1/M 

A = np.array(globalnaMatrica)
B = np.array(vektorDesneStrane)

rjesenje = np.linalg.solve(A, B)

x = np.linspace(1, 2, M)       #returns evenly spaced numbers over a specified interval.

plt.plot(x, rjesenje, color='blue')             #draw points (markers) in a diagram


plt.plot(x, -(1 / 6) * x ** 3 + (7 / 6) * x - 1, color='red')

plt.show()