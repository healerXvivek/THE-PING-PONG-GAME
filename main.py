from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.title("                                 The Ping Pong Game ")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

r_pad = Paddle((370, 0))
l_pad = Paddle((-370, 0))

ball = Ball()
score = ScoreBoard()

screen.listen()
screen.onkey(r_pad.go_up, "Up")
screen.onkey(r_pad.go_down, "Down")
screen.onkey(l_pad.go_up, "w")
screen.onkey(l_pad.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    # collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_wall()

    # collision with paddle
    if ball.distance(r_pad) < 55 and ball.xcor() > 350 or ball.distance(l_pad) < 55 and ball.xcor() < -350:
        ball.bounce_paddle()

    # missing the l_pad
    if ball.xcor() > 420:
        ball.reset_position()
        score.l_point()

    # missing the r_pad
    if ball.xcor() < -420:
        ball.reset_position()
        score.r_point()

screen.exitonclick()
