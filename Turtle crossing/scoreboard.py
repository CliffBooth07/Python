from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-250, 250)
        self.stage_level = 1
        self.write(f"Level: {self.stage_level}", align='left', font=FONT)

    def level(self):
        self.stage_level += 1
        # print(self.level)
        self.clear()
        self.write(f"Level: {self.stage_level}", align='left', font=FONT)

    def gameover(self):
        self.goto(0, 0)
        self.write("GAME OVER", align='center', font=FONT)
