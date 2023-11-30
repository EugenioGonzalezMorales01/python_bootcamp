import time
from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        #self.penup()
        self.shape("circle")
        self.color("white")
        self.x_move = 10
        self.y_move = 10

    def start_moving(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def y_bouncing(self):
        self.y_move *= -1

    def x_bouncing(self):
        self.x_move *= -1
        return 0.02

    def reset_position(self):
        self.setposition(0,0)
        self.start_moving()
