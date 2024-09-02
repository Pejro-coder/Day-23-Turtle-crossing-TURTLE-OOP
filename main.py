import time
import random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# Setup game screen
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
screen.bgcolor("black")

# setup starting player object, scoreboard and starting cars
player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()
car_manager.starting_cars(40, -300)

# player controls
screen.onkeypress(player.move, "Up")
# screen.onkeypress(player.move_back, "s")


game_is_on = True
while game_is_on:
    time.sleep(0.05)
    scoreboard.show_score()
    screen.update()

    # create new cars and remove old cars from screen
    for car in car_manager.cars:
        if car.xcor() < -320:
            car_manager.cars.remove(car)
            car.hideturtle()
            x_spawn_position = random.randint(320, 340)
            car_manager.new_car(x_spawn_position)

        # check colision with "cars"
        if player.distance(car) < 20:
            player.reset_position()
            car_manager.reset_move_speed()
            scoreboard.game_over()
            screen.update()
            time.sleep(1.5)
            scoreboard.reset_position()
            scoreboard.clear()

        # winning condition
        if player.ycor() > 300:
            player.reset_position()
            car_manager.increase_move_speed()
            scoreboard.increase_level()
            print(car_manager.move_speed)
            time.sleep(1.5)
    car_manager.move_cars()
