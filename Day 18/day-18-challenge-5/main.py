import turtle
from turtle import Turtle, Screen
import random

tim = Turtle()
turtle.colormode(255)
tim.speed("fastest")


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


for angle in range(0, 360, 5):
    tim.color(random_color())
    tim.setheading(angle)
    tim.circle(100)

screen = Screen()
screen.exitonclick()