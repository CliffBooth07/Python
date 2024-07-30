from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.score = 0
        self.highscore=0
        self.goto(0, 270)
        self.score_line()




    def score_line(self):
        self.clear()
        f=open("data.txt","r")
        self.highscore=f.read()
        self.write(f"Score : {self.score} HighScore : {self.highscore}", align="center", font=('Arial', 15, 'normal'))

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER", align="center", font=('Arial', 15, 'normal'))
    def reset_game(self):
        f = open("data.txt", "w")
        if self.score>int(self.highscore):
            self.highscore=self.score
            f.write(str(self.score))
        self.score=0
        self.score_line()
        f.close()

    def add_score(self):
        self.score += 1

        self.score_line()
