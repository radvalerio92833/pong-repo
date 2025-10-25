from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__(shape="circle")
        self.color("white")
        self.penup()
        self.x = 10
        self.y = 10
        self.move_speed = 0.1

    def move(self):
        y = self.ycor() + self.y
        x = self.xcor() + self.x
        self.goto(x, y)

    def bouncey(self):
        self.y *= -1

    def bouncex(self):
        self.x *= -1
        self.move_speed *= 0.9

    def reset_ball(self):
        self.goto(0, 0)
        self.bouncex()
        self.move_speed = 0.1


