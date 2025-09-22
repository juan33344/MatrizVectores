def determinante_sarrus(matriz):
    if len(matriz) != 3 or any(len(fila) != 3 for fila in matriz):
        raise ValueError("La matriz debe ser de 3x3")

    a11, a12, a13 = matriz[0]
    a21, a22, a23 = matriz[1]
    a31, a32, a33 = matriz[2]

    # Suma de diagonales principales
    suma = (a11 * a22 * a33) + (a12 * a23 * a31) + (a13 * a21 * a32)

    # Suma de diagonales inversas
    resta = (a13 * a22 * a31) + (a11 * a23 * a32) + (a12 * a21 * a33)

    return suma - resta


# Ejemplo
matriz = [
    [2, 3, 1],
    [4, 1, 5],
    [7, 2, 6]
]

print("Determinante =", determinante_sarrus(matriz))

import numpy as np

# Definir la matriz como arreglo de numpy
A = np.array([
    [2, 3, 1],
    [4, 1, 5],
    [7, 2, 6]
])

# Determinante con numpy    
det = np.linalg.det(A)
print("Determinante con NumPy =", round(det))

