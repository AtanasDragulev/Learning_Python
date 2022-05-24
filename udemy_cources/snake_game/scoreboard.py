from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 15, "bold")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.score = 0
        with open("data.txt", mode="r") as file:
            self.high_score = int(file.read())
        self.goto(x=0, y=270)
        self.score = 0
        self.hideturtle()
        self.update_board()

    def update_board(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as file:
                file.write(str(self.high_score))
        self.score = 0
        self.update_board()

    def increase_score(self):
        self.score += 1
        self.update_board()

