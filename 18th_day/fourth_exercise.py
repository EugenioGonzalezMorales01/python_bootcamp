from turtle import Turtle, Screen
import random

jimmy = Turtle()
jimmy.speed("fastest")
Screen().colormode(255)

def random_color():
    r_color = random.randint(0, 255)
    g_color = random.randint(0, 255)
    b_color = random.randint(0, 255)
    return r_color, g_color, b_color
def draw_circle():
    jimmy.pencolor(random_color())
    jimmy.circle(100)

def draw_spirograph(desviation):
    for _ in range(int(360/desviation)):
        draw_circle()
        print(jimmy.heading())
        jimmy.setheading(jimmy.heading() + desviation)

draw_spirograph(desviation=5)

Screen().exitonclick()
