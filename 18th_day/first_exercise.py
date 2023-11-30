from turtle import Turtle, Screen

my_turtle = Turtle()
my_screen = Screen()
steps = 10

for x in range(4):
    for x in range(steps):
        if x % 2 != 0:
            my_turtle.pendown()
        elif x % 2 == 0:
            my_turtle.penup()
        my_turtle.fd(10)
    my_turtle.lt(90)