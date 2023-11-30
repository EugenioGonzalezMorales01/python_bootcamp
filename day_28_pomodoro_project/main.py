from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
marks = ""
timer = None

# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    global marks
    global reps
    marks = ""
    reps = 0
    title_lb.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")


def start_timer():
    global reps

    WORK_SEC = WORK_MIN * 60
    SHORT_BREAK_SEC = SHORT_BREAK_MIN * 60
    LONG_BREAK_SEC = LONG_BREAK_MIN * 60
    reps += 1

    # work time/short break time/long break time
    if reps < 12 and reps % 2 != 0:
        title_lb.config(text="Work Time", fg=GREEN)
        count_down(WORK_SEC)
    elif reps < 12 and reps % 2 == 0:
        title_lb.config(text="Short Break Time", fg=PINK)
        count_down(SHORT_BREAK_SEC)
    elif reps == 12:
        title_lb.config(text="Long Break Time", fg=RED)
        count_down(LONG_BREAK_SEC)


def count_down(count):
    global reps
    global marks

    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        if reps % 2 == 0:
            marks += "✅"
        chk_mark.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=10, bg=YELLOW)
window.minsize(width=300, height=400)

# Label | Title
title_lb = Label(text="Timer", font=(FONT_NAME, 30, "bold"))
title_lb.config(bg=YELLOW, fg=GREEN)
title_lb.grid(column=1, row=0)

# Canvas | Timer
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# Button | Start
st_btn = Button(text="Start", command=start_timer)
st_btn.grid(column=0, row=2)

# Button | Reset
rs_btn = Button(text="Reset", command=reset_timer)
rs_btn.grid(column=2, row=2)

# Label | Check
chk_mark = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 14, "bold"))
chk_mark.grid(column=1, row=3)

window.mainloop()
