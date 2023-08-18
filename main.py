from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))
ball = Ball()
score = Scoreboard()


screen.listen()
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    if ball.xcor() > 320:
        if abs(ball.ycor() - r_paddle.ycor()) < 50:
            ball.paddle_bounce()
        elif ball.xcor() > 350:
            ball.reset_ball()
            score.l_point()

    if ball.xcor() < -320:
        if abs(ball.ycor() - l_paddle.ycor()) < 50:
            ball.paddle_bounce()
        elif ball.xcor() < -350:
            ball.reset_ball()
            score.r_point()





screen.exitonclick()