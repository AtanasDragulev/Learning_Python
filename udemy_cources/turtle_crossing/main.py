import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
scoreboard = Scoreboard()
player = Player()
screen.listen()
screen.onkeypress(player.move_up, "Up")
cars = CarManager()


game_is_on = True
loop = 1
speed = 0.1
while game_is_on:
    cars.new_car()
    time.sleep(speed)
    screen.update()
    cars.move()
    if cars.check_collision(player.pos()):
        game_is_on = False
    if player.ycor() > 280:
        player.next_level()
        scoreboard.update_score()
        speed *= 0.80


screen.exitonclick()