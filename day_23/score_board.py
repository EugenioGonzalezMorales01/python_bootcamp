from turtle import Turtle

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(0, 230)
        self.score = 0
        self.color("black")
        self.update_score()

    def update_score(self, new_score=0):
        self.score = new_score
        self.clear()
        self.write(arg=f"SCORE: {self.score}", align="center", font=("Arial", 14, "normal"))

    def get_score(self):
        return self.score