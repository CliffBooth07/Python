import time
from turtle import Turtle,Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
screen=Screen()
screen.title("Snake Game")
screen.setup(600,600)
screen.bgcolor("black")
food=Food()
scoreboard=Scoreboard()
snake=Snake()


screen.tracer(0)

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

is_game_on=True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.snake_move()
    if snake.head.distance(food)<15:
        food.food_random()
        scoreboard.add_score()
        snake.extends()

    if snake.head.xcor()>280 or snake.head.xcor()<-280 or snake.head.ycor()>280 or snake.head.ycor()<-280:
        # is_game_on=False
        scoreboard.reset_game()
        snake.snake_reset()

    for parts in snake.snake[1:]:
        # if parts==snake.head:
        #     pass
        if snake.head.distance(parts)<5:
            # is_game_on = False
            scoreboard.reset_game()
            snake.snake_reset()




screen.exitonclick()