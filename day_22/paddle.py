from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, x_position, y_position):
        super().__init__()
        self.shape("square")
        self.penup()
        self.setheading(270)
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.color("white")
        self.speed(4)
        self.setposition(x_position, y_position)

    def head_up(self):
        self.backward(40)

    def head_down(self):
        self.forward(40)
