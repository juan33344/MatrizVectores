import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import solve

# Coificientes de las Ecuaciones
A = np.array([[3, 2], [4, 1]])
#Constantes de la ecuacion
b = np.array([5, 6])

# Solucion de sistemas de ecuaciones
solucion = solve(A, b)
print("solución del sistema: X=", solucion[0], "; Y=", solucion[1])
# Graficar las ecuaciones
x = np.linspace(-1, 3, 400)
y1 = (5 - 3*x) / 2
y2 = (6 - 4*x) 
plt.plot(x, y1, label='3X + 2Y = 5')
plt.plot(x, y2, label='4X + 1Y = 6')
plt.scatter(solucion[0], solucion[1], color='red', label='Solución (X,Y)')
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.grid(True)
plt.legend()
plt.show()
plt.title('Sistema de Ecuaciones')
