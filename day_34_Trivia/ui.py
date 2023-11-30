import time
from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizzInterface:
    def __init__(self, quiz: QuizBrain):

        self.quizz_brain = quiz
        self.score = 0
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # Score Label
        self.score_lab = Label(text=f"Score: 0", background=THEME_COLOR, foreground="white")
        self.score_lab.grid(column=1, row=0, pady=(0, 20))

        # Canvas
        self.canvas = Canvas(width=400, height=300, bg="white")
        self.canvas_text = self.canvas.create_text(
            200, 150, text="",
            width=300,
            font=("Arial", 20, "italic"),
            fill=THEME_COLOR)
        self.canvas.grid(column=0, row=1, columnspan=2)

        # True Button
        t_img = PhotoImage(file="images/true.png")
        self.t_btn = Button(image=t_img, bg=THEME_COLOR, command=self.true_button_pressed)
        self.t_btn.grid(column=0, row=2, pady=(20, 0))

        # False Button
        f_img = PhotoImage(file="images/false.png")
        self.f_btn = Button(image=f_img, bg=THEME_COLOR, command=self.false_button_pressed)
        self.f_btn.grid(column=1, row=2, pady=(20, 0))

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quizz_brain.still_has_questions():
            q_text = self.quizz_brain.next_question()
            self.canvas.itemconfig(self.canvas_text, text=q_text)
            self.score_lab.config(text=f"Score: {self.score}/{len(self.quizz_brain.question_list)}")
        else:
            self.canvas.itemconfig(self.canvas_text,
                                   text=f"Your final score is: {self.score}/{len(self.quizz_brain.question_list)}")
            self.t_btn.config(state=DISABLED)
            self.f_btn.config(state=DISABLED)

    def true_button_pressed(self):
        if self.quizz_brain.check_answer("True"):
            self.color_answered(True)
            self.score += 1
        else:
            self.color_answered(False)

    def false_button_pressed(self):
        if self.quizz_brain.check_answer("False"):
            self.color_answered(True)
            self.score += 1
        else:
            self.color_answered(False)

    def color_answered(self, asw: bool):
        if asw:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(500, self.get_next_question)



