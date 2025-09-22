import turtle

def dibujar_hexagono():
    turtle.begin_fill()
    for _ in range(6):
        turtle.forward(50)
        turtle.left(60)
    turtle.end_fill()

def dibujar_panal():
    for _ in range(6):
        dibujar_hexagono()
        turtle.forward(50)
        turtle.right(60)

turtle.shape("turtle")
turtle.color("orange", "yellow")
turtle.speed(0)
turtle.pensize(5)

# Primer panal
turtle.penup()
turtle.goto(-200, 200)
turtle.pendown()
dibujar_panal()

# Segundo panal en otra posición
turtle.penup()
turtle.goto(100, -100)
turtle.pendown()
dibujar_panal()

turtle.done()