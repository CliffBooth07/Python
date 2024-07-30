from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("circle")
        self.shapesize(1, 1)
        self.corx = 20
        self.cory = 20
        self.speed_of_ball = 0.2

    def ball_move(self):
        self.goto(x=self.xcor() + self.corx, y=self.ycor() + self.cory)

    def bounce_updown_side(self):
        self.cory *= -1
        print(f"y in upsidedown: {self.cory}")

    def bounce_platform(self):
        self.corx *= -1
        print(f"x in platfrom {self.corx}")

    def ball_respawn(self):
        self.goto(0, 0)
        self.cory *= -1
        self.corx *= -1
        print(f"in respawn {self.corx}, {self.cory}")

    def ball_speed(self):
        self.speed_of_ball *= 0.9
