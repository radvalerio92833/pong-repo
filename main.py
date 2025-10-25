from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Score
import time

screen = Screen()
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
screen.setup(width=800,height=600)

paddle1 = Paddle(-350, 0)
paddle2 = Paddle(350, 0)

ball = Ball()

score = Score()

screen.listen()
screen.onkey(paddle1.move_up, "w")
screen.onkey(paddle2.move_up, "Up")
screen.onkey(paddle1.move_down, "s")
screen.onkey(paddle2.move_down, "Down")
game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bouncey()
    if (ball.distance(paddle2) < 50 and ball.xcor() > 320) or ball.distance(paddle1) < 50 and ball.xcor() < -320:
        ball.bouncex()
    if ball.xcor() > 380:
        ball.reset_ball()
        score.increase_l_score()
    if ball.xcor() < -380:
        ball.reset_ball()
        score.increase_r_score()
screen.exitonclick()