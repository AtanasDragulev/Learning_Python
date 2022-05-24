from turtle import Turtle
import time

POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20


class Snake:

    def __init__(self):
        self.blocks = []
        self.create_snake()
        self.head = self.blocks[0]

    def create_snake(self):
        for pos in POSITIONS:
            self.add_segment(pos)

    def go_up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def go_left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def go_right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def go_down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def move_snake(self):

        for part in range(len(self.blocks) - 1, 0, -1):
            self.blocks[part].setpos(self.blocks[part - 1].pos())
        self.head.forward(MOVE_DISTANCE)
        time.sleep(0.1)

    def add_segment(self, _position):
        new_segment = Turtle(shape="square")
        new_segment.penup()
        new_segment.color("white")
        new_segment.setpos(_position)
        self.blocks.append(new_segment)

    def extend(self):
        self.add_segment(self.blocks[-1].position())

    def reset(self):
        for block in self.blocks:
            block.goto(1000, 1000)
        self.blocks.clear()
        self.create_snake()
        self.head = self.blocks[0]
