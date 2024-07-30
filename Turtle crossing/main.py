import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()
screen.listen()
screen.onkeypress(player.movement, "space")
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.car_gen()
    car_manager.speed_car()
    if player.condition():
        # print("level inc")
        player.default_pos()
        scoreboard.level()
        car_manager.level_up()

    for car in car_manager.cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.gameover()

screen.exitonclick()
