from random import random, randint
from window import window
import turtle
import math

def generate_vector():
    d = [ -0.2, 0.2 ]
    return {
        'x': d[math.floor(random() * len(d))],
        'y': d[math.floor(random() * len(d))]
    }

class Paddle:
    def __init__(self, x, y):
        player = turtle.Turtle()
        player.speed(0)
        player.penup()
        player.shape("square")
        player.color("#fff")
        player.shapesize(stretch_wid=5, stretch_len=1)
        player.goto(x, y)

        self.player = player

    def get_coords(self):
        return [
            self.player.xcor(),
            self.player.ycor()
        ]

    def listen(self, key, callback):
        def wrapper():
            callback(self.player)
        window.listen()
        window.onkeypress(wrapper, key)        

class Ball:
    def __init__(self, x, y):
        ball = turtle.Turtle()
        ball.speed(0)
        ball.penup()
        ball.shape("square")
        ball.color("#fff")
        ball.goto(x, y)

        self.ball = ball
        self.vector = generate_vector()

    def get_coords(self):
        return [
            self.ball.xcor(),
            self.ball.ycor()
        ]

    def invert(self, coordinate):
        self.vector[coordinate] *= -1

    def update(self):
        self.ball.setx(self.ball.xcor() + self.vector['x'])
        self.ball.sety(self.ball.ycor() + self.vector['y'])

    def boundary(self):
        (x, y) = self.get_coords()
        score = "none"

        if x >= 390:
            self.ball.goto(0, 0)
            self.vector = generate_vector()
            score = "player_1"
        
        if x <= -390:
            self.ball.goto(0, 0)
            self.vector = generate_vector()
            score = "player_2"

        if y >= 290 or y <= -290:
            self.invert("y")

        return score

    def collision(self, paddles):
        (x, y) = self.get_coords()

        for paddle in paddles:
            (paddle_x, paddle_y) = paddle.get_coords() 
            dist_x = abs(paddle_x - x)
            if y <= paddle_y + 50 and y >= paddle_y - 50 and dist_x <= 20 and dist_x >= 0:
                self.invert('x')
                self.invert('y')