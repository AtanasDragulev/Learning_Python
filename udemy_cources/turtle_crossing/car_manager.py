from turtle import Turtle
import random


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():

    def __init__(self):
        self.cars = []

    def move(self):
        car = 0
        while car < (len(self.cars)):
            self.cars[car].forward(STARTING_MOVE_DISTANCE)
            if self.cars[car].xcor() < -320:
                self.cars.pop(car)
            else:
                car += 1

    def check_collision(self, player_coord):
        for car in self.cars:
            if car.distance(player_coord) < 18:
                return True

    def new_car(self):
        if random.randint(1,6) == 1:
            new_car = Turtle("square")
            y_position = random.randint(-250, 250)
            new_car.penup()
            new_car.shapesize(1, 2)
            new_car.color(random.choice(COLORS))
            new_car.setheading(180)
            new_car.goto(x=300, y=y_position)
            self.cars.append(new_car)
