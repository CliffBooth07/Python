from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)
        self.shape("turtle")
        self.color("green")

    def movement(self):
        self.forward(MOVE_DISTANCE)

    def condition(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False

    def default_pos(self):
        self.goto(STARTING_POSITION)
