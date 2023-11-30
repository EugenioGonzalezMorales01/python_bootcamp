from turtle import Turtle

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.speed("fastest")
        self.color("white")
        self.setposition(0, 230)
        self.score = 0
        if open("C:/Users/eugen/Documents/Python Projects Save Data/hs.txt").read() != "":
            self.high_score = open("C:/Users/eugen/Documents/Python Projects Save Data/hs.txt").read()
        else:
            self.high_score = 0
        self.set_score()

    def set_score(self, current_score=0):
        self.score = current_score
        self.clear()
        self.write(f"Score = {self.score} | High Score = {self.high_score}", False, align="center", font=('Arial', 14, 'normal'))

    def reset(self):
        if self.score >=  int(self.high_score):
            self.high_score = self.score
        self.score = 0
        self.set_score()
        file = open("C:/Users/eugen/Documents/Python Projects Save Data/hs.txt", "r+")
        file.truncate(0)
        content = file.write(str(self.high_score))
        file.close()


