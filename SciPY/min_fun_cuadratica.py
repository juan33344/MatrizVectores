from scipy.optimize import minimize
import matplotlib.pyplot as plt
import numpy as np

#Diferenciamos la funcion Cuadratica
def funcion(x):
    return x**2 - 4*x +4

#Optimizacion de la funcion 
resultado = minimize(funcion, x0 = 0)
print(f"Minimo de la Funcion x = {resultado.x[0]}")

#Graficamos la funcion 
x= np.linspace(-2, 4,400)
y= funcion(x)

plt.plot(x,y ,label='f(x)=x^2 - 4x +4')
plt.scatter(resultado.x,funcion(resultado.x), color='red', label='minimo')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(True)
plt.legend()
plt.show()

s