import colorgram, random
from turtle import Turtle, Screen

jim = Turtle()
jim.penup()
jim.speed(0)
jim.hideturtle()
sc = Screen()
sc.colormode(255)


def get_color_palette():
    colors = colorgram.extract('img/image.jpg', 30)
    rgb_colors = []

    for color in colors:
        rgb_colors.append((color.rgb[0], color.rgb[1], color.rgb[2]))
    return rgb_colors


def draw_dot(position, color_pal):
    jim.setposition(position[0], position[1])
    jim.dot(20, random.choice(color_pal))


def draw_art():
    color_pal = get_color_palette()
    for y in range(-250, 250, 50):
        for x in range(-250, 250, 50):
            draw_dot(position=(x, y), color_pal=color_pal)



draw_art()
sc.exitonclick()
