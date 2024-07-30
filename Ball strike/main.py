from turtle import Screen
from platform import Platform
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
ball = Ball()
scoreboard = Scoreboard()
screen.tracer(0)
platform1 = Platform((380, 0))
platform2 = Platform((-380, 0))

screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong")

screen.listen()
screen.onkeypress(platform1.up, "Up")
screen.onkeypress(platform1.down, "Down")

screen.onkeypress(platform2.up, "w")
screen.onkeypress(platform2.down, "s")

is_game_on = True
while is_game_on:

    screen.update()
    time.sleep(ball.speed_of_ball)
    ball.ball_move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_updown_side()

    if ball.xcor() > 350 and ball.distance(platform1) < 50 or ball.xcor() < -350 and ball.distance(platform2) < 50:
        ball.bounce_platform()
        ball.ball_speed()

    elif ball.xcor() > 380:
        ball.ball_respawn()
        scoreboard.update_player2()
        ball.speed_of_ball = 0.2

    elif ball.xcor() < -380:
        ball.ball_respawn()
        scoreboard.update_player1()
        ball.speed_of_ball = 0.2

screen.exitonclick()
