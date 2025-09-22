import numpy as np

def determinante_clasico(matriz):
    """
    Calcula el determinante de una matriz de 3x3 usando el método clásico.
    """
    # Verificar si la matriz es de 3x3
    if len(matriz) != 3 or any(len(fila) != 3 for fila in matriz):
        raise ValueError("La matriz debe ser de 3x3")

    a, b, c = matriz[0]
    d, e, f = matriz[1]
    g, h, i = matriz[2]

    # Determinante de las submatrices de 2x2
    det1 = e * i - h * f
    det2 = d * i - g * f
    det3 = d * h - g * e

    # Cálculo final del determinante
    determinante = a * det1 - b * det2 + c * det3
    return determinante

# Inicializar la matriz usando numpy
matriz_ejemplo = np.array([[1, 3, 9],
                          [2, 5, 7],
                          [1, 2, 3]])

# Calcular el determinante
det_calculado = determinante_clasico(matriz_ejemplo)

# Verificar el resultado con numpy
det_numpy = np.linalg.det(matriz_ejemplo)

print(f"Matriz de ejemplo:\n{matriz_ejemplo}")
print(f"Determinante calculado con el método clásico: {det_calculado}")
print(f"Determinante verificado con numpy: {det_numpy}")
print(f"Los resultados coinciden: {np.isclose(det_calculado, det_numpy)}")