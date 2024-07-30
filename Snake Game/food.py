from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.speed("fastest")
        self.shapesize(0.5,0.5)
        self.penup()
        self.food_random()


    def food_random(self):
        randx=random.randint(-280,280)
        randy=random.randint(-280,280)
        self.goto(randx,randy)
