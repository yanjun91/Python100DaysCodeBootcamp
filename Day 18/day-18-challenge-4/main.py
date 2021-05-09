import turtle
from turtle import Turtle, Screen
import random

# Random walk
tim = Turtle()
turtle.colormode(255)
tim.speed("fastest")
tim.pensize(15)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


angles = [0, 90, 180, 270]

for _ in range(100):
    angle = random.choice(angles)
    tim.color(random_color())
    tim.setheading(angle)
    tim.forward(20)

screen = Screen()
screen.exitonclick()
