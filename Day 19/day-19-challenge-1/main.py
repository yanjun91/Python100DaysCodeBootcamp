from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()
angle = 0


def move_forwards():
    tim.forward(10)


def move_backwards():
    tim.backward(10)


def turn_anticlockwise():
    global angle
    angle += 5
    tim.setheading(angle)
    # tim.setheading(tim.heading + 5)


def turn_clockwise():
    global angle
    angle -= 5
    tim.setheading(angle)
    # tim.setheading(tim.heading - 5)


def reset_canvas():
    tim.reset()


screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=turn_anticlockwise)
screen.onkey(key="d", fun=turn_clockwise)
screen.onkey(key="c", fun=reset_canvas)

screen.exitonclick()