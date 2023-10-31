from turtle import Turtle

class Ball(Turtle):

            def __init__(self):
                super().__init__()
                self.penup()
                self.color("white")
                self.shape("circle")
                self.speed("slowest")
                self.x_move = 10
                self.y_move = 10
                self.flip = 1
                self.move_speed = 0.1


            def move(self):

                new_x = self.xcor() + self.flip * self.x_move
                new_y = self.ycor() + self.y_move
                self.goto(new_x, new_y)


            def bounce_y(self):
                self.y_move *= -1

            def bounce_x(self):
                self.x_move *= -1
                #increases speed everytime the ball hits a paddle
                self.move_speed *= 0.9
