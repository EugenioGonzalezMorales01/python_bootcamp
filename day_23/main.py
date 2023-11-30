import random
import time
from turtle import Screen
from my_turtle import myTurtle
from car import Car
from score_board import ScoreBoard

sc = Screen()
sc.setup(width=600, height=600)
sc.tracer(0)
sc.listen()
sc.title("Jerry's cross road game")

jerry = myTurtle()
sc.onkey(fun=jerry.go_up, key="w")
sc.onkey(fun=jerry.go_down, key="s")
sc.onkey(fun=jerry.go_right, key="d")
sc.onkey(fun=jerry.go_left, key="a")

cars = [[],[],[],[],[],[],[],[],[],[]]
CAR_COLORS = ["blue", "yellow", "cyan", "brown", "green", "purple", "pink", "red", "blue", "green"]
CAR_SEPARATIONS = [250, 370, 200]

score_board = ScoreBoard()
score = 0


for x in range(10):
    for y in range(3):
        if y == 0:
            x_cord = -200 + (y + random.randint(-50, 10))
        else:
            x_cord = cars[x][y-1].xcor() + random.choice(CAR_SEPARATIONS) + random.randint(0, 50)
        y_cord = -200 + (x * 40)
        print(f"{x}:{x_cord} {y}:{y_cord}")
        car = Car(CAR_COLORS[x], x_cord,  y_cord)
        cars[x].append(car)

gaming = True
while gaming:
    time.sleep(0.1)
    sc.update()

    for i in range(10):
        for j in range(3):
            cars[i][j].move(i)
            if cars[i][j].ycor() == jerry.ycor():
                if cars[i][j].distance(jerry) < 20:
                    jerry.die()
                    sc.update()
                    time.sleep(0.5)
                    jerry.reset()
                    score_board.update_score(0)


    if jerry.ycor() >= 180:
        score += 1
        score_board.update_score(score)
        jerry.reset()
        for i in range(10):
            for j in range(3):
                cars[i][j].increase_speed(score_board.get_score())


sc.exitonclick()