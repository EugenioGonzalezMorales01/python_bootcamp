import random
from turtle import Turtle

class Car(Turtle):

    def __init__(self, color, x_cor, y_cor):
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.color(color)
        self.goto(x_cor, y_cor)
        self.setheading(180)
        self.speed = 5

    def move(self, car_num):
        if car_num % 2 == 0:
            self.forward(self.speed)

            if self.xcor() < -300:
                self.goto(250, self.ycor())
        else:
            self.backward(self.speed)

            if self.xcor() > 300:
                self.goto(-250, self.ycor())

    def increase_speed(self, score):
        self.speed += score
