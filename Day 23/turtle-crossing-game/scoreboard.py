from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.title = "Level: "
        self.hideturtle()
        self.level = 1
        self.penup()
        self.goto(-280, 260)
        self.refresh_level()

    def refresh_level(self):
        super().write(self.title + str(self.level), align="left", font=FONT)

    def increase_level(self):
        self.level += 1
        super().clear()
        self.refresh_level()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)
