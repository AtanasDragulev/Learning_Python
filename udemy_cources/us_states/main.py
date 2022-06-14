import turtle
import csv

import coordinates

with open("50_states.csv") as states:
    states = csv.reader(states)
    states_dict = {state[0]: {"coordinates": (int(state[1]), int(state[2])),"Found": False} for state in states if state[0] != "state"}


screen = turtle.Screen()
screen.title("USA States Game")
screen.setup(width=725, height=491)
screen.bgpic("blank_states_img.gif")
turtle = turtle.Turtle()
turtle.penup()

found = []
while len(found) < 50:
    answer = screen.textinput(f"{len(found)}/{len(states_dict)} states correct", "Input state:")
    if not answer:
        continue
    answer = answer.title()
    if answer == "Exit":
        break
    if answer in found:
        continue
    if answer in states_dict:
        turtle.goto(states_dict[answer]["coordinates"])
        turtle.write(answer)
        found.append(answer)
        states_dict[answer]["Found"] = True

with open("result.csv", mode="w") as csv_file:
    for state in states_dict:
        if not states_dict[state]["Found"]:
            csv_file.write(f"{state},{states_dict[state]['coordinates']}\n")
