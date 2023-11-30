import time
from turtle import Screen
from ball import Ball
from paddle import Paddle
from score_board import ScoreBoard


def move_l(paddle):
    sc.onkey(fun=paddle.head_up, key="w")
    sc.onkey(fun=paddle.head_down, key="s")

def move_r(paddle):
    sc.onkey(fun=paddle.head_up, key="i")
    sc.onkey(fun=paddle.head_down, key="k")


sc = Screen()
sc.bgcolor("black")
sc.setup(width=800, height=600)
sc.title("pong")
sc.tracer(0)
sc.listen()

paddle_1 = Paddle(-350, 0)
paddle_2 = Paddle(350, 0)

score_board = ScoreBoard()

move_l(paddle_1)
move_r(paddle_2)

ball = Ball()

ball_speed = 0.1
gaming = True
while gaming:
    time.sleep(ball_speed)
    ball.start_moving()
    sc.update()

    if ball.position()[1] >= 280 or ball.position()[1] <= -280:
        ball.y_bouncing()

    #Detect collision with right/left paddle
    if ball.position()[0] > 330 or ball.position()[0] < -330:
        if ball.distance(paddle_2) < 50 or ball.distance(paddle_1) < 50:
            print("Made contact")
            ball_speed -= ball.x_bouncing()
        else:
            if ball.xcor() > 330:
                score_board.update_score(1)
            else:
                score_board.update_score(2)
            ball.reset_position()
            ball_speed = 0.1
sc.exitonclick()