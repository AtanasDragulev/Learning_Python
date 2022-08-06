import turtle
import random

colors = [(202, 164, 110), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20),
          (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165),
          (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129),
          (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]
painter = turtle.Turtle()


screen = turtle.Screen()
screen.setup(500, 500)
painter.screen.colormode(255)
painter.speed(0)
painter.hideturtle(), painter.penup()
painter.goto(-230, -230)
painter.showturtle()


def paint(_row, _column):
    row = 0
    while row != _row:
        row += 1
        painter.dot(20, random.choice(colors))
        for _ in range(_column - 1):
            painter.forward(50)
            painter.dot(20, random.choice(colors))
        direction = painter.heading()
        painter.setheading(90)
        painter.forward(50)
        painter.setheading(direction + 180)


paint(10,10)

screen.exitonclick()
