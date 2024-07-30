from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.score1 = 0
        self.score2 = 0
        self.scorecard()
        # self.player2()

    def scorecard(self):
        self.goto(100, 200)
        self.write(f"{self.score1}", align="center", font=('Arial', 50, 'normal'))
        self.goto(-100, 200)
        self.write(f"{self.score2}", align="center", font=('Arial', 50, 'normal'))

    # def player2(self):

    def update_player1(self):
        self.clear()
        self.score1 += 1
        self.scorecard()

    def update_player2(self):
        self.clear()
        self.score2 += 1
        self.scorecard()
