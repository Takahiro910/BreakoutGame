from turtle import Turtle

BLOCK_POSITIONS = [
    (-280,200), (-210,200), (-140,200), (-70,200), (0,200), (70,200), (140,200), (210,200), (280,200)
    , (-280,150), (-210,150), (-140,150), (-70,150), (0,150), (70,150), (140,150), (210,150), (280,150)
    , (-280,100), (-210,100), (-140,100), (-70,100), (0,100), (70,100), (140,100), (210,100), (280,100)
    , (-280,50), (-210,50), (-140,50), (-70,50), (0,50), (70,50), (140,50), (210,50), (280,50)
    , (-280,0), (-210,0), (-140,0), (-70,0), (0,0), (70,0), (140,0), (210,0), (280,0)
    ]


class Block():
    def __init__(self):
        self.blocks = []
        self.create_blocks()

    def create_blocks(self):
        for position in BLOCK_POSITIONS:
            self.create_block(position)

    def create_block(self, position):
        new_block = Turtle("square")
        new_block.shapesize(stretch_wid=2, stretch_len=3)
        new_block.color("white")
        new_block.penup()
        new_block.goto(position)
        self.blocks.append(new_block)

    def reset(self):
        for block in self.blocks:
            block.goto(1800, 1800)
        self.blocks.clear()
        self.create_blocks()

