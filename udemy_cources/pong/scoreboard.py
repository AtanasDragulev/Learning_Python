from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()

        self.l_score = 0
        self.r_score = 0
        self.goto(0, 240)
        self.update_board()

    def update_board(self):
        self.clear()
        self.write(f"{self.l_score} : {self.r_score}", align="center", font=("courier", 40, "bold"))