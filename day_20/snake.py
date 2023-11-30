import time
from turtle import Turtle

UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:
    def __init__(self, sc, food, score):
        self.sc = sc
        self.sc.listen()
        self.limit = 250
        self.sc.setup(width=self.limit * 2, height=self.limit * 2)
        self.sc.bgcolor("black")
        self.sc.title("Snake Game")
        self.sc.tracer(0)
        self.limits = [self.limit, self.limit * -1]
        self.snake_segments = []
        self.segments_positions = [(0, 0), (-20, 0), (-40, 0), (-60, 0), (-80, 0), (-100, 0)]
        self.food = food
        self.score = score

    def set_up_snake(self):
        for snake_segment in range(6):
            self.snake_segments.append(Turtle(shape="square"))
            self.snake_segments[snake_segment].penup()
            self.snake_segments[snake_segment].color("white")
            self.snake_segments[snake_segment].setposition(self.segments_positions[snake_segment])

    def reset_snake(self):
        for segment in self.snake_segments:
            segment.goto(1000, 1000)
        self.snake_segments.clear()
        self.set_up_snake()

    def turn_up(self):
        if self.snake_segments[0].heading() != DOWN:
            self.snake_segments[0].setheading(UP)

    def turn_down(self):
        if self.snake_segments[0].heading() != UP:
            self.snake_segments[0].setheading(DOWN)

    def turn_right(self):
        if self.snake_segments[0].heading() != LEFT:
            self.snake_segments[0].setheading(RIGHT)

    def turn_left(self):
        if self.snake_segments[0].heading() != RIGHT:
            self.snake_segments[0].setheading(LEFT)

    def set_heading(self):
        self.sc.onkeypress(fun=self.turn_up, key="w")
        self.sc.onkeypress(fun=self.turn_down, key="s")
        self.sc.onkeypress(fun=self.turn_right, key="d")
        self.sc.onkeypress(fun=self.turn_left, key="a")

    def detect_walls(self):
        if abs(self.snake_segments[0].position()[0]) > 250 or abs(self.snake_segments[0].position()[1]) > 250:
            return False
        else:
            return True

    def grow_snake(self):
        self.snake_segments.append(Turtle(shape="square"))
        self.snake_segments[len(self.snake_segments)-1].penup()
        self.snake_segments[len(self.snake_segments) - 1].setposition(self.snake_segments[len(self.snake_segments) - 2].position())
        self.snake_segments[len(self.snake_segments) - 1].color("white")

    def check_tail_colision(self):
        for snake_segment in self.snake_segments[1:]:
            if self.snake_segments[0].distance(snake_segment) < 10:
                return True


    def move(self, gaming=True, score=0):
        while gaming:
            self.sc.update()
            time.sleep(0.1)
            for snake_segment in range(len(self.snake_segments) - 1, 0, -1):
                self.snake_segments[snake_segment].setposition(self.snake_segments[snake_segment-1].position())
            self.snake_segments[0].forward(20)
            moving = self.detect_walls()
            if self.snake_segments[0].distance(self.food) < 15:
                score += self.food.refresh()
                print(score)
                self.score.set_score(score)
                self.grow_snake()
            if self.check_tail_colision():
                moving = False
            if moving == False:
                self.score.reset()
                self.reset_snake()
                score = 0



