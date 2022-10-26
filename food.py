from turtle import Turtle
import random


class Food(Turtle):
    """
    This class inherits from the super class Turtle and it will define the food located in random points in the screen
    every time the snake collides with the food.
    """

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("red")
        self.speed("fastest")
        self.refresh_food_point()

    def refresh_food_point(self):
        x_point = random.randint(-280, 260)
        y_point = random.randint(-280, 260)
        self.goto(x_point, y_point)
