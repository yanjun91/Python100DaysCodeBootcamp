from turtle import Turtle

ALIGN = "center"
FONT = ("Courier", 12, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.title = "Score: "
        self.color("white")
        self.hideturtle()
        self.score = 0
        self.penup()
        self.goto(0, 280)
        self.refresh_score()

    def refresh_score(self):
        super().write(self.title + str(self.score), align=ALIGN, font=FONT)

    def increment_score(self):
        self.score += 1
        super().clear()
        self.refresh_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGN, font=FONT)