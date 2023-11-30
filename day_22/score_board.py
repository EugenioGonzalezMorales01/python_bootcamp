from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.setposition(0, 230)
        self.color("white")
        self.player1_score = 0
        self.player2_score = 0
        self.update_score()

    def update_score(self, player=0):
        if player == 1:
            self.player1_score += 1
        elif player == 2:
            self.player2_score += 1
        self.clear()
        self.write(arg=f"Score = {self.player1_score} | {self.player2_score}", align="center",
                   font=("Arial", 14, "normal"))
        print("Hello")
