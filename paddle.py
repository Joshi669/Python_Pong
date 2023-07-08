from turtle import Turtle

WIDTH = 20
HEIGHT = 100
X_POS = 100
Y_POS = 0


class Paddle(Turtle):
    def __init__(self):
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=WIDTH, stretch_len=HEIGHT)
        self.penup()
        self.goto(X_POS, Y_POS)

