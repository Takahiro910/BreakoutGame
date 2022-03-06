from turtle import Screen
from paddle import Paddle
from ball import Ball
from board import Board
from block import Block
import turtle


def motion(event):
    x, y = event.x, event.y
    paddle.setx(x-400)


screen = Screen()
screen.screensize(800, 600)
screen.bgcolor("black")
screen.title("BreakOut Game")
screen.tracer(0)

game_title = turtle
game_title.color("#00dbb4")
game_title.penup()
game_title.hideturtle()
game_title.write("The Breakout", False, "center", font=("Arial", 85, "bold"))

paddle = Paddle((0, -280))
ball = Ball()
board = Board()
wall_block = Block()

canvas = screen.getcanvas()
canvas.bind('<Motion>', motion)

game_is_on = True
while game_is_on:
    screen.update()
    ball.move()
    board.write_score()

    # wall reflection
    if ball.xcor() > 360 or ball.xcor() < -360:
        ball.x_reflection()
    if  ball.ycor() > 290:
        ball.y_reflection()

    # paddle reflection
    if -275 < ball.ycor() < -265 and abs(paddle.xcor()-ball.xcor()) < 30:
        ball.y_reflection()

    # block reflection
    for block in wall_block.blocks:
        block_x = block.xcor()
        block_y = block.ycor()
        if abs(block_x - ball.xcor()) < 30 and abs(block_y - ball.ycor()) < 30:
            wall_block.blocks.remove(block)
            block.goto(1800, 1800)
            ball.y_reflection()
            board.score += 1
            board.clear()
            board.write_score()
        elif abs(block_y - ball.ycor()) < 20 and abs(block_x - ball.xcor()) < 40:
            wall_block.blocks.remove(block)
            block.goto(1800, 1800)
            ball.x_reflection()
            board.score += 1
            board.clear()
            board.write_score()

    # game clear
    if board.score % 45 == 0:
        wall_block.reset()

    # game over
    if ball.ycor() < -290:
        ball.reset_position()
        wall_block.reset()
        board.reset()

screen.exitonclick()