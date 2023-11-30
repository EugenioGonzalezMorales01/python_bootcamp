from turtle import Screen
from food import Food
from score_board import ScoreBoard
import snake

sc = Screen()

my_food = Food()
my_score = ScoreBoard()
my_snake = snake.Snake(sc, my_food, my_score)


my_snake.set_up_snake()
my_snake.set_heading()
my_snake.move()

sc.exitonclick()
