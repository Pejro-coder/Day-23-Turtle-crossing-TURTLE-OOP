from turtle import Turtle, position
import random

MOVE_SPEED = 2
INCREMENT = 2

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]


class CarManager():
    def __init__(self):
        self.cars = []
        self.move_speed = MOVE_SPEED

    # New car
    def new_car(self, x_position):
        car = Turtle(shape="square")
        car.penup()
        car.color(random.choice(COLORS))
        car.shapesize(1, 1.8)
        y_position = random.randint(-230, 300)
        car.goto(x_position, y_position)
        self.cars.append(car)

    # creating start game cars
    def starting_cars(self, difficulty, x_from):
        '''difficulty = number of cars,
        x_from = cars left most spawning position'''
        for _ in range(difficulty):
            x_range = random.randint(x_from, 350)
            self.new_car(x_range)

    # Move all cars forward
    def move_cars(self):
        for car in range(len(self.cars)):
            self.cars[car].backward(self.move_speed)

    # Level speed increase
    def increase_move_speed(self):
        self.move_speed += INCREMENT

    def reset_move_speed(self):
        self.move_speed = MOVE_SPEED
