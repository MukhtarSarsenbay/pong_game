from turtle import Turtle
import random


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.vel = 0.1

    def move(self):
        x_cor = self.xcor()+self.x_move
        y_cor = self.ycor()+self.y_move
        self.goto(x_cor, y_cor)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.vel *= 0.9

    def reset(self):
        self.home()
        self.vel = 0.1
        self.bounce_x()
