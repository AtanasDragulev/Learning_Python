from turtle import Turtle, Screen, color
import random

screen = Screen()
screen.setup(width=500, height=400)
screen.bgcolor("gray")
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color:").lower()
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []
for _color in colors:
    turtles.append(Turtle(shape="turtle"))
    turtles[-1].penup()
    turtles[-1].color(_color)

turtles[0].goto(x=-210, y=-160)
for current in range(1, len(turtles)):
    turtles[current].goto(x=-210, y=turtles[current - 1].ycor() + 65)

is_race_on = False

if user_bet:
    is_race_on = True
winner = ""
while is_race_on:
    for current_turtle in turtles:
        steps = random.randint(0, 50)
        current_turtle.forward(steps)
        if current_turtle.xcor() >= 210:
            is_race_on = False
            winner = current_turtle.pencolor()
            
if user_bet == winner:
    print(f"You win. The winner is: {winner}")
else:
    print(f"You loose. The winner is: {winner}")
screen.exitonclick()
