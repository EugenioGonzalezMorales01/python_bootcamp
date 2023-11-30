from turtle import Turtle, Screen

CIRCLE_DEGREES = 360
SIDE_SIZE = 100

form_sides = 3
timmy = Turtle()
main_screen = Screen()
turtle_colors = ["CornflowerBlue", "DarkSeaGreen", "Khaki", "SaddleBrown", "Brown", "RosyBrown", "DeepPink", "DarkSlateBlue"]

def draw_figure(sides):
    for side in range(sides):
        timmy.forward(SIDE_SIZE)
        timmy.right(CIRCLE_DEGREES/sides)
    sides += 1

for side_num in range(3,11):
    timmy.pencolor(turtle_colors[side_num-3])
    draw_figure(sides=side_num)


main_screen.exitonclick()
