from tkinter import *


def button_clicked():
    my_label["text"] = u_input.get()

# Window
window = Tk()
window.title("My first program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# Label
my_label = Label(text="I'm a Label", font=("Arial", 24, "bold"))
# This two lines does the same thing
my_label["text"] = "New Text"
my_label.config(text="New Text")
my_label.grid(column=0, row=0)
my_label.config(padx=50, pady=50)

# Button
my_button = Button(text="Click Me", command=button_clicked)
my_button.grid(column=1, row=1)

# New Button
my_button2 = Button(text="I'm useless :D")
my_button2.grid(column=2, row=0)

# Entry
u_input = Entry(width=10)
u_input.grid(column=4, row=3)

window.mainloop()
