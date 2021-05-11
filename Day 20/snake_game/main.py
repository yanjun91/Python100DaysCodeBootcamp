from turtle import Screen,  Turtle
import time
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
# To turn off animation,
# then call the screen.update() once all segments move so that we wont see each segment moving one at a time
screen.tracer(0)

snake = Snake()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    # Update all segments at once after move forward
    screen.update()
    # To delay the screen refresh update of the segments. If no add delay, it will be too fast for us to notice
    time.sleep(0.1)
    snake.move()

screen.exitonclick()
