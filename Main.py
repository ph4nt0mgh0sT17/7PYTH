import turtle
import random

# Window of the turtle
window = turtle.Screen()

# Background color of the window
window.bgcolor('white')

# Creting the turtle
t = turtle.Turtle()
t.speed(40)


forward_speed = 200
angle_change = 90

t.fillcolor('blue')

t.begin_fill()

for i in range(150):
    for i in range(4):
        t.forward(forward_speed)
        t.left(angle_change)

    t.left(angle_change -random.randint(0, 200))

t.end_fill()

window.exitonclick()
