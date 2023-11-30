from turtle import Turtle, Screen

jim = Turtle()
sc = Screen()


def move_fd():
    jim.forward(5)


def move_bk():
    jim.back(5)


def turn_right():
    jim.setheading(jim.heading() - 5)


def turn_left():
    jim.setheading(jim.heading() + 5)


def clear_screen():
    jim.clear()
    jim.penup()
    jim.home()
    jim.pendown()


sc.listen()
sc.onkeypress(key="w", fun=move_fd)
sc.onkeypress(key="s", fun=move_bk)
sc.onkeypress(key="d", fun=turn_right)
sc.onkeypress(key="a", fun=turn_left)
sc.onkeypress(key="c", fun=clear_screen)
sc.exitonclick()
