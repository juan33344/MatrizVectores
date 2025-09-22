import turtle

# Configuración inicial
screen = turtle.Screen()
screen.bgcolor("lightgray")
screen.title("Pingüino Simple y Correcto")
screen.setup(width=800, height=600)

t = turtle.Turtle()
t.speed(8)
t.pensize(3)

def ir_a(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

# 1. CUERPO PRINCIPAL - Óvalo negro uniforme (subido)
ir_a(0, -20)
t.color("black", "black")
t.begin_fill()
t.setheading(0)
# Óvalo vertical uniforme usando shear transformation
import math
for angle in range(360):
    # Crear óvalo - más alto que ancho
    x = 70 * math.cos(math.radians(angle))
    y = 100 * math.sin(math.radians(angle))
    if angle == 0:
        t.goto(x, y - 20)
    else:
        t.goto(x, y - 20)
t.end_fill()

# 2. VIENTRE BLANCO - Óvalo blanco más pequeño (subido)
ir_a(0, 0)
t.color("black", "white")
t.begin_fill()
t.setheading(0)
# Óvalo blanco uniforme más pequeño
for angle in range(360):
    x = 50 * math.cos(math.radians(angle))
    y = 70 * math.sin(math.radians(angle))
    if angle == 0:
        t.goto(x, y)
    else:
        t.goto(x, y)
t.end_fill()

# 3. ALETA IZQUIERDA - Conectada al cuerpo, sin separación
ir_a(-50, 10)
t.color("black", "black")
t.begin_fill()
t.setheading(200)  # Ángulo hacia abajo-izquierda
t.forward(45)
t.left(70)
t.forward(30)
t.left(70)
t.forward(45)
t.end_fill()

# 4. ALETA DERECHA - Conectada al cuerpo, sin separación
ir_a(50, 10)
t.color("black", "black")
t.begin_fill()
t.setheading(340)  # Ángulo hacia abajo-derecha
t.forward(45)
t.right(70)
t.forward(30)
t.right(70)
t.forward(45)
t.end_fill()

# 5. PIE IZQUIERDO - Óvalo naranja (ajustado)
ir_a(-35, -120)
t.color("black", "orange")
t.begin_fill()
t.setheading(0)
for _ in range(2):
    t.circle(30, 90)
    t.circle(12, 90)
t.end_fill()

# 6. PIE DERECHO - Óvalo naranja (ajustado)
ir_a(35, -120)
t.color("black", "orange")
t.begin_fill()
t.setheading(0)
for _ in range(2):
    t.circle(30, 90)
    t.circle(12, 90)
t.end_fill()

# 7. OJO IZQUIERDO - Círculo blanco
ir_a(-25, 60)
t.color("black", "white")
t.begin_fill()
t.circle(20)
t.end_fill()

# 8. OJO DERECHO - Círculo blanco
ir_a(25, 60)
t.color("black", "white")
t.begin_fill()
t.circle(20)
t.end_fill()

# 9. PUPILA IZQUIERDA - Círculo negro pequeño
ir_a(-20, 70)
t.color("black", "black")
t.begin_fill()
t.circle(7)
t.end_fill()

# 10. PUPILA DERECHA - Círculo negro pequeño
ir_a(20, 70)
t.color("black", "black")
t.begin_fill()
t.circle(7)
t.end_fill()

# 11. PICO - Triángulo naranja simple
ir_a(-10, 35)
t.color("black", "orange")
t.begin_fill()
t.goto(10, 35)   # Base del triángulo
t.goto(0, 20)    # Punta hacia abajo
t.goto(-10, 35)  # Cerrar triángulo
t.end_fill()

# Ocultar turtle
t.hideturtle()

# Título
ir_a(-200, 150)
t.color("blue")
t.write("Pingüino usando coordenadas (x,y)", font=("Arial", 18, "bold"))

print("¡Pingüino listo! Haz clic para cerrar.")
screen.exitonclick()