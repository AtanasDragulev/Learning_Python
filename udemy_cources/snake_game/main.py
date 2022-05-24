from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time


screen = Screen()
screen.tracer(0)
screen.setup(width=600, height=600)
screen.bgcolor("black")
score = Scoreboard()
snake = Snake()

new_food = Food()

screen.listen()
screen.onkey(snake.go_up, "Up")
screen.onkey(snake.go_left, "Left")
screen.onkey(snake.go_right, "Right")
screen.onkey(snake.go_down, "Down")

game_is_on = True

while game_is_on:

    screen.update()

    snake.move_snake()
    if snake.head.distance(new_food) < 15:
        new_food.refresh()
        score.increase_score()
        snake.extend()

    if abs(snake.head.xcor()) >= 290 or abs(snake.head.ycor()) >= 290:
        score.game_over()
        snake.reset()

    for block in snake.blocks[1:]:
        if snake.head.distance(block) < 10:
            score.game_over()
            # game_is_on = False

screen.exitonclick()
