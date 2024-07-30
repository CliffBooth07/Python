from turtle import Turtle


class Platform(Turtle):
    def __init__(self, location):
        super().__init__()
        self.color("white")
        self.penup()
        self.shape("square")
        self.shapesize(5, 1)
        self.goto(location)
        # self.ycor=0

    def up(self):
        self.sety(y=self.ycor() + 20)

    def down(self):
        self.sety(y=self.ycor() - 20)
