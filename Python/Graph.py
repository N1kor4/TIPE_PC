# Cire1 :
import numpy as np

uL50 = [8.76, 9.75, 10.47, 9.65, 9.44]
uL100 = [11.52, 11.29, 11, 10.75, 11.64]
uL150 = [13.52, 11.32, 12.66, 13.03, 12.58]
uL200 = [17.13, 16.3, 16.78, 14.64, 15.1]

uL = [uL50, uL100, uL150, uL200]
UL = [50, 100, 150, 200]

# Moyennes
M = [np.mean(uL[i]) for i in range(len(uL[0]) - 1)]
print("La moyenne de l'angle d'arrachement pour un volume de " + str(UL[0]) + "uL est de " + str(round(M[0], 2)))

# Variance
V = []
for i in range(len(uL)):
    s = 0
    for j in range(i - 1):
        s = + (uL[i][j] - M[j]) ** 2
    V.append(np.sqrt(s / len(uL[0])))
    print("L'ecart type de cet angle pour un volume de " + str(UL[i]) + "uL est de " + str(round(V[i], 2)))

import matplotlib.pyplot as plt

plt.figure()
plt.grid()
plt.plot(UL, uL, '+')
plt.xlabel('Volume des gouttelettes en micro Litre')
plt.ylabel('Angle des gouttes')
plt.title("Evolution de l'angle d'arrachement en fonction du volume")
plt.plot(UL, M)
plt.show()
