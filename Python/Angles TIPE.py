import numpy as np
import matplotlib.pyplot as plt

# Angles d'arrachement


V = [200, 150, 100, 50]

B200 = [8.76, 9.75, 10.47, 9.65, 9.44]
B150 = [11.52, 11.29, 11, 10.75, 11.64]
B100 = [13.52, 11.32, 12.66, 13.03, 12.58]
B50 = [17.13, 16.3, 16.78, 14.64, 15.1]
B = [B200, B150, B100, B50]
MoyB = [np.mean(B[0]), np.mean(B[1]), np.mean(B[2]), np.mean(B[3])]
uB = [np.std(B[0], ddof=1), np.std(B[1], ddof=1), np.std(B[2], ddof=1), np.std(B[3], ddof=1)]

E200 = [17.96, 16, 15.73, 12.69, 15.45]
E150 = [20.12, 19, 19.51, 16.95, 18.76]
E100 = [23.9, 21, 20.66, 20.38, 19.89]
E50 = [27.95, 26, 27.48, 26.66, 25.82]
E = [E200, E150, E100, E50]
MoyE = [np.mean(E[0]), np.mean(E[1]), np.mean(E[2]), np.mean(E[3])]
uE = [np.std(E[0], ddof=1), np.std(E[1], ddof=1), np.std(E[2], ddof=1), np.std(E[3], ddof=1)]

figure = plt.figure(figsize=(10, 4))

plt.subplot(121)
plt.plot(V, MoyB, 'ob')
plt.errorbar(V, MoyB, yerr=uB, fmt=',k')
plt.ylabel("Angles d'arrachements en °")
plt.xlabel("Volume en μL")
plt.title("Cire de Bougie")
plt.suptitle("Évolution de l'angle d'arrachement en fonction du volume")
plt.grid()

plt.subplot(122)
plt.plot(V, MoyE, 'ob')
plt.errorbar(V, MoyE, yerr=uE, fmt=',k')
plt.ylabel("Angles d'arrachements en °")
plt.xlabel("Volume en μL")
plt.title("Cire à épiler")
plt.suptitle("Évolution de l'angle d'arrachement en fonction du volume")
plt.grid()

plt.show()

# Angles de contact à l'équilibre


Cires = ["Bougie", "Suie", "Cire à épiler", "Cire pour chaussures", "Cire d'abeille"]
B = [127.5, 124.5, 121, 123.5, 125, 120, 118.5, 124.5, 127.5, 122.5]
S = [141.5, 140, 138.5, 144.5, 136.5, 132, 140.5, 137, 137, 139.5]
E = [110, 112.25, 119.5, 113, 116, 111.5, 112.5, 109.5, 108, 108.5]
C = [27, 30, 28.5, 26, 29.5, 30, 27.5, 32, 31.5, 27]
A = [108, 114.5, 111, 110, 113.5, 112, 109.5, 114, 110.5, 109]

M = [B, S, E, C, A]

MoyM = [np.mean(M[0]), np.mean(M[1]), np.mean(M[2]), np.mean(M[3]), np.mean(M[4])]
uM = [np.std(M[0], ddof=1), np.std(M[1], ddof=1), np.std(M[2], ddof=1), np.std(M[3], ddof=1), np.std(M[4], ddof=1)]

figure = plt.figure(figsize=(10, 4))

plt.plot(Cires, MoyM, 'bo', markersize=2)
plt.errorbar(Cires, MoyM, yerr=uM, fmt=',k')
plt.ylabel("Angles de contact à l'équilibre en °")
plt.xlabel("Différentes cires")
plt.title("Différents angles de contact à l'équilibre")
plt.grid()

plt.plot(Cires, [90] * len(Cires), "r", label="Angle limite π/2")
plt.legend(loc="upper right")
plt.show()
