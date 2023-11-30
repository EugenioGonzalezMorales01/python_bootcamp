from turtle import Turtle

class myTurtle(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(0,-240)
        self.setheading(90)
        self.shape("turtle")
        self.y_step = 40
        self.x_step = 20

    def go_up(self):
        self.setheading(90)
        self.forward(self.y_step)

    def go_down(self):
        self.setheading(270)
        self.forward(self.y_step)

    def go_right(self):
        self.setheading(0)
        self.forward(self.x_step)

    def go_left(self):
        self.setheading(180)
        self.forward(self.x_step)

    def reset(self):
        self.color("black")
        self.goto(0, -240)

    def die(self):
        self.color("red")
