from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, x, y):
        super().__init__(shape="square")
        self.speed("fastest")
        self.penup()
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(x, y)

    def move_up(self):
        if self.ycor() <= 220:
            y = self.ycor() + 20
        self.sety(y)

    def move_down(self):
        if self.ycor() >= -220:
            y = self.ycor() - 20
        self.sety(y)



