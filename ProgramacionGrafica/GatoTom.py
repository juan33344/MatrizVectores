import turtle

# Configuración de la pantalla
screen = turtle.Screen()
screen.setup(width=600, height=800)
screen.bgcolor("lightgray")
screen.title("Dibujando un pingüino con Turtle - ¡Imagen Final Perfecta!")

t = turtle.Turtle()
t.speed(0)
t.penup()

# --- Funciones auxiliares para dibujar formas ---
def draw_circle(x, y, radius, color, border_color="black"):
    t.penup()
    t.goto(x, y - radius)
    t.pendown()
    t.fillcolor(color)
    t.pencolor(border_color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

# --- Dibujar las partes del pingüino ---

# 1. Cuerpo y barriga
draw_circle(0, -110, 150, "black") # Cuerpo
draw_circle(0, -70, 110, "white")  # Barriga


# 2. Cabeza (ajustada ligeramente más abajo para mejor integración)
draw_circle(0, 130, 90, "black") # Cabeza


# 3. Ojos (ajustados a la nueva posición de la cabeza)
# Ojo derecho
draw_circle(40, 170, 30, "white")
draw_circle(40, 185, 12, "black")

# Ojo izquierdo
draw_circle(-40, 170, 30, "white")
draw_circle(-40, 185, 12, "black")


# 4. Pico (¡Arreglado para ser idéntico al del imagen!)
t.penup()
t.goto(0, 80) # Punto central superior del pico, ajustado
t.pendown()
t.fillcolor("yellow")
t.pencolor("black")
t.begin_fill()
t.setheading(270) # Apunta hacia abajo
t.forward(45) # Longitud del pico
t.setheading(200) # Gira para el lado izquierdo (ángulo más abierto)
t.forward(60)
t.setheading(340) # Gira para el lado derecho (ángulo más abierto)
t.forward(60)
t.end_fill()


# 5. Alas (¡Arregladas para ser idénticas al del imagen!)
# Ala izquierda
t.penup()
t.goto(-155, -10) # Punto de inicio del ala, más abajo y cerca del cuerpo
t.pendown()
t.fillcolor("black")
t.pencolor("black")
t.begin_fill()
t.setheading(160) # Ángulo inicial más horizontal
t.circle(180, 50) # Curva exterior del ala, más pronunciada
t.setheading(240) # Ángulo inferior para la curva de regreso
t.circle(100, 40) # Curva interior
t.goto(-155, -10) # Cierra el ala
t.end_fill()

# Ala derecha (simétrica a la izquierda)
t.penup()
t.goto(155, -10) # Punto de inicio del ala
t.pendown()
t.fillcolor("black")
t.pencolor("black")
t.begin_fill()
t.setheading(20) # Ángulo inicial más horizontal
t.circle(-180, 50) # Curva exterior del ala
t.setheading(-60) # Ángulo inferior para la curva de regreso
t.circle(-100, 40) # Curva interior
t.goto(155, -10) # Cierra el ala
t.end_fill()


# 6. Patas (ya estaban bien, sin cambios)
draw_circle(-40, -230, 40, "yellow")
draw_circle(40, -230, 40, "yellow")


t.hideturtle()
turtle.done()