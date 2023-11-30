import random
from turtle import Turtle, Screen

sc = Screen()

sc.setup(width=500, height=500)
jim = []
colors = ["red", "green", "blue", "pink", "yellow", "purple"]
user_bet = sc.textinput(title="Turtle Racing!", prompt="Which color of turtle will win the racing?")


def paint_goal():
    painter = Turtle()
    painter.hideturtle()
    painter.penup()
    painter.setposition((sc.screensize()[0] / 2) + 15, 75)
    painter.setheading(-90)
    painter.pendown()
    painter.forward(180)


def insert_turtles():
    for turtle_index in range(0, 6):
        jim.append(Turtle(shape="turtle"))
        set_up_turtle(turtle_index)


def at_goal(turtle):
    if turtle.color()[0] == user_bet:
        should_continue = sc.textinput("Congrats! Your turtle has won!", "Do you wanna start another race? (y/n) ")
    else:
        should_continue = sc.textinput(f"So sad :( the turtle {turtle.color()[0]} has won",
                                       "Do you want a revenge? >:) (y/n) ")

    if should_continue == "y":
        play(another_race=True)
    else:
        exit()


def start_racing():
    x = 0
    while x == 0:
        for turtle in jim:
            move_distance = random.randint(0, 30)
            if turtle.position()[0] >= (sc.screensize()[0] / 2) - 30:
                turtle.setposition(sc.screensize()[0] / 2, turtle.position()[1])
            else:
                turtle.forward(move_distance)
            if turtle.position()[0] >= sc.screensize()[0] / 2:
                at_goal(turtle)


def set_turtle_position(turtle_index):
    jim[turtle_index].penup()
    jim[turtle_index].setposition(-230, -90 + (turtle_index * 30))


def set_up_turtle(turtle_index):
    jim[turtle_index].color(colors[turtle_index])
    set_turtle_position(turtle_index)


def play(another_race=False):
    if another_race:
        for x in range(0, len(jim)):
            set_up_turtle(x)
    else:
        insert_turtles()

    start_racing()


paint_goal()
play()
sc.exitonclick()
