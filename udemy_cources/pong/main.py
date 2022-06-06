from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


screen = Screen()
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)
screen.bgcolor("black")
screen.update()
scoreboard = Scoreboard()
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()

screen.listen()

screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")
score_l = 0
score_r = 0
game_is_on = True
sleep_time = 0.1

while game_is_on:
    time.sleep(sleep_time)
    screen.update()
    ball.move()
    screen.update()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    if ball.xcor() > 320 or ball.xcor() < -320:
        if ball.distance(l_paddle) < 50 or ball.distance(r_paddle) < 50:
            ball.hit()
            sleep_time *= 0.9
        elif abs(ball.xcor()) > 400:
            if ball.xcor() < -400:
                scoreboard.l_score += 1
            elif ball.xcor() > 400:
                scoreboard.r_score += 1
            sleep_time = 0.1
            ball.reset_ball()
            scoreboard.update_board()


screen.exitonclick()
