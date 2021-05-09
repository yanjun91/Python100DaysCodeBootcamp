from turtle import Turtle, Screen
# Draw dashed line
tim = Turtle()

# for _ in range(10):
#     tim.forward(10)
#     tim.color("white")
#     tim.forward(10)
#     tim.color("black")

for _ in range(10):
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown()

screen = Screen()
screen.exitonclick()