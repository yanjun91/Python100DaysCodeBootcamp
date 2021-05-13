import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random


def set_position():
    random_x = random.randint(320, 500)
    random_y = random.randint(-250, 280)
    return random_x, random_y


def generate_car():
    coord = set_position()
    new_car = CarManager(coord)
    cars.append(new_car)


screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing")
screen.tracer(0)

scoreboard = Scoreboard()
player1 = Player()
car_manager = CarManager()
cars = []

screen.listen()
screen.onkeypress(fun=player1.move, key="Up")
count = 0

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move()

    # Detect collision with car
    for car in car_manager.all_cars:
        if car.distance(player1) < 20:
            scoreboard.game_over()
            game_is_on = False

    # Detect turtle reach finish line
    if player1.reach_finish_line():
        player1.restart_position()
        car_manager.increase_speed()
        scoreboard.increase_level()

screen.exitonclick()
