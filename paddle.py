from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, Position):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.color("white")
        self.penup()
        self.speed("fastest")
        self.setposition(Position)