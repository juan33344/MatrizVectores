from scipy.integrate import quad
import numpy as np
import matplotlib.pyplot as plt

#Definimos la funcion
def funcion(x):
    return np.sin(x)
#Calculo de la Integral

integral , error = quad(funcion, 0, np.pi)
print(f"Valor de la Integral ", integral)

#Graficamos la funcion
x = np.linspace(0, np.pi, 400)
y = funcion(x)

plt.plot(x, y, label='f(x)=sin(x)')
plt.fill_between(x, y, color='lightblue', label='Área bajo la curva')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(True)
plt.legend()
plt.show()



