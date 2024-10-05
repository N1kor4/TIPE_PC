import numpy as np
import matplotlib.pyplot as plt

r = np.array([6.048, 6.302, 6.624, 7.232, 7.441, 7.996, 8.813, 9.364, 12.459, 13.831, 15.9, 16.7])

costeta = np.cos(np.array([1.18, 1.256, 1.43, 1.53, 1.553, 1.675, 1.745, 1.797, 1.955, 1.98, 2.007, 2.007]))

g = -1 + (4.5/r)*(0.75 + 1)

plt.title("Rugosité en fonction de cos(θ*)")
plt.plot(r,g, label='modèle théorique')
plt.scatter(r, costeta, s=3, c='red', label = 'Valeurs expérimentales')
plt.xlabel('Rugosité')
plt.ylabel('cos(θ*) en rad')
plt.legend()
plt.grid()
plt.show()