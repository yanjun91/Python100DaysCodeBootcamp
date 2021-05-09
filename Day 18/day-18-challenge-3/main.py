from turtle import Turtle, Screen
import random

# Draw triangle, square, pentagon, hexagon, heptagon, octagon, nonagon and decagon overlapping each others
tim = Turtle()

for sides in range(3, 11):
    angle = 360/sides
    R = random.random()
    B = random.random()
    G = random.random()
    tim.color(R, G, B)
    for side in range(sides):
        tim.right(angle)
        tim.forward(100)

screen = Screen()
screen.exitonclick()