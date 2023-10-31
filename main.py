from turtle import Screen
import time
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
#screen.trace(0) stops the animations from occuring until screen.update() is called
screen.tracer(0)
scoreboard = ScoreBoard()

r_paddle = Paddle("r")
l_paddle = Paddle("l")
ball = Ball()

screen.update()
screen.listen()

end = False
while end == False:
    #time.sleep() stops after each loop for a specified interval
    time.sleep(ball.move_speed)
    screen.update()
    screen.onkey(r_paddle.move_up, "Up")
    screen.onkey(r_paddle.move_down, "Down")
    screen.onkey(l_paddle.move_up, "w")
    screen.onkey(l_paddle.move_down, "s")
    ball.move()
    #detect collision with top and bottom of screen
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    #detect collision with paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        print("made contact with paddle")
        ball.bounce_x()
    #detect if ball does out of bounds
    if ball.xcor() > 380:
        scoreboard.update("r")
        ball.goto(0,0)
        ball.flip *= -1
        ball.move_speed = 0.1
    if ball.xcor() < -380:
        scoreboard.update("l")
        ball.goto(0,0)
        ball.flip *= -1
        ball.move_speed = 0.1





screen.exitonclick()