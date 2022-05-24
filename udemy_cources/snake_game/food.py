from turtle import Turtle
import random

COLORS = ["yellow", "green", "blue", "red"]


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        # self.color(random.choice(COLORS))
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        self.color(random.choice(COLORS))
        self.goto(random.randint(-280, 280), random.randint(-280, 280))