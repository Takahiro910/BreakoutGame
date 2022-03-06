from turtle import Turtle
import time
import random
SLEEP_TIME = 0.01

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.sleep_time = SLEEP_TIME
        self.x_move = random.choice([-5,5])
        self.y_move = 5
        self.goto(0, -250)

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)
        time.sleep(self.sleep_time)

    def y_reflection(self):
        self.y_move *= -1

    def x_reflection(self):
        self.x_move *= -1
        self.sleep_time *= 0.9

    def reset_position(self):
        self.goto(0, -250)
        self.y_reflection()
        self.x_reflection()
        self.sleep_time = SLEEP_TIME