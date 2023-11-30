from turtle import Turtle, Screen
import random

STEPS = 50
TURTLE_COLORS = ["CornflowerBlue", "DarkSeaGreen", "Khaki", "SaddleBrown", "Brown", "RosyBrown", "DeepPink", "DarkSlateBlue"]

jimmy = Turtle()
jimmy.pensize(10)
jimmy.speed(10)
main_screen = Screen()
main_screen.colormode(255)

def random_color():
    r_color = random.randint(0, 255)
    g_color = random.randint(0, 255)
    b_color = random.randint(0, 255)
    return r_color, g_color, b_color

def draw_line():
    my_tuple = random_color()

    jimmy.pencolor(my_tuple)
    jimmy.forward(STEPS)
    for turns in range(random.randint(1, 4)):
        jimmy.right(90)

for x in range(100):

    draw_line()

main_screen.exitonclick()



