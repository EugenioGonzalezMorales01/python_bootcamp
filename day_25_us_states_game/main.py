import csv
import time
import turtle
import pandas

sc = turtle.Screen()
sc.title("U.S. States Games")
image = "blank_states_img.gif"
sc.addshape(image)
sc.setup(width=800, height=800)
turtle.shape(image)
asw_list = []
states_data = pandas.read_csv("50_states.csv")
pointer = turtle.Turtle()
pointer.penup()
pointer.hideturtle()
remaining_states = []

print(states_data)

def message(message, color, won):
    pointer.goto(0, 100)
    pointer.color(color)
    pointer.write(f"{message}", font=("Arial", 20, "normal"), align="center")
    if won == False:
        time.sleep(0.8)
        pointer.undo()
    pointer.color("black")

repeated_state = True
guessed_states = []
while len(guessed_states) < 50:
    while repeated_state:
        asw = sc.textinput(title=f"{len(guessed_states)}/50 states guessed", prompt="Type the name of the state :)").title()
        if asw == "Exit":
            break
        if asw not in asw_list:
            asw_list.append(asw)
            repeated_state = False
        else:
            message("REPEATED STATE", "red", False)
    if asw == "Exit":
        break
    elif asw in states_data.state.to_list():
        x_cor = int(states_data.x[states_data.state == asw])
        y_cor = int(states_data.y[states_data.state == asw])
        pointer.goto(x_cor, y_cor)
        pointer.write(arg=asw)
        guessed_states.append(asw)
    else:
        message(f"'{asw}' IS NOT A STATE", "red", False)
    repeated_state = True

if len(guessed_states) == 50:
    message("You won!", "blue", True)
else:
    for state in states_data.state.to_list():
        if state not in guessed_states:
            remaining_states.append(state)
    remaining_states = pandas.DataFrame(remaining_states, columns=["ghvghv"])
    remaining_states.to_csv("remaining_states")




turtle.mainloop()
