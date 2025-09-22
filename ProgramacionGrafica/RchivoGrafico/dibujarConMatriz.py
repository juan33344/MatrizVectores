import numpy as np
from turtle import *

# Matriz del emoji carita feliz
A = np.array([
    [2,2,2,2,2,2,2,2,2,2],
    [2,0,0,0,0,0,0,0,0,2],
    [2,0,1,0,0,0,0,1,0,2],
    [2,0,1,1,0,0,1,1,0,2],
    [2,0,0,0,0,0,0,0,0,2],
    [2,0,1,0,0,0,0,1,0,2],
    [2,0,0,1,1,1,1,0,0,2],
    [2,0,0,0,0,0,0,0,0,2],
    [2,0,0,0,0,0,0,0,0,2],
    [2,2,2,2,2,2,2,2,2,2],
])

# Tamaño de cada celda
tam = 20

# Posición inicial del dibujo
x0 = -100
y0 = 100

# Función para dibujar un cuadrado (borde)
def cuadrado(lado, x, y, color_cuadro="green"):
    penup()
    goto(x, y)
    pendown()
    color(color_cuadro)
    begin_fill()
    for _ in range(4):
        forward(lado)
        right(90)
    end_fill()
    penup()

# Función para dibujar un círculo (ojos, boca)
def circulo(radio, x, y, color_circulo="yellow"):
    penup()
    goto(x + radio, y - radio)  # Centrado
    pendown()
    color(color_circulo)
    begin_fill()
    circle(radio)
    end_fill()
    penup()

# Preparar turtle
speed(0)
hideturtle()
bgcolor("white")

# Recorrer la matriz y dibujar
for i in range(A.shape[0]):
    for j in range(A.shape[1]):
        x = x0 + j * tam
        y = y0 - i * tam
        if A[i][j] == 2:
            cuadrado(tam, x, y)
        elif A[i][j] == 1:
            circulo(tam // 2, x, y)

done()


