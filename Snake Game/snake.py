from turtle import Turtle

coordinate = [(0, 0), (-20, 0), (-40, 0)]
SPEED = 20
UP=90
DOWN=270
LEFT=180
RIGHT=0

class Snake:
    def __init__(self):
        self.snake = []
        self.create_snake()
        self.head=self.snake[0]

    def create_snake(self):
        for coor in coordinate:
            self.snake_parts(coor)

    def snake_reset(self):
        for part in self.snake:
            part.goto(1000,1000)
        self.snake.clear()
        self.create_snake()
        self.head = self.snake[0]

    def snake_parts(self,coor):
        dummy = Turtle(shape="square")
        dummy.color("white")
        dummy.penup()
        dummy.goto(coor)
        self.snake.append(dummy)



    def extends(self):
        self.snake_parts(self.snake[-1].position())

    def snake_move(self):
        for parts in range(len(self.snake) - 1, 0, -1):
            xcoor = self.snake[parts - 1].xcor()
            ycoor = self.snake[parts - 1].ycor()
            self.snake[parts].goto(xcoor, ycoor)
        self.head.forward(SPEED)

    def up(self):
        if self.head.heading()!=DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
