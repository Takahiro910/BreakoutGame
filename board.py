import turtle
from turtle import Turtle
FONT = ("alias", 20, "normal")


class Board(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score = 0
        with open("data.txt") as file:
            self.highscore = int(file.read())
        self.game_is_on = False

    def write_score(self):
        self.clear()
        self.goto(-250, 250)
        self.write(f"SCORE: {self.score}\nHIGH SCORE: {self.highscore}", move=False, align="center", font=FONT)

    def reset(self):
        if self.score > self.highscore:
            with open("data.txt", "w") as file:
                file.write(str(self.score))
            self.highscore = self.score
        self.score = 0
        self.write_score()