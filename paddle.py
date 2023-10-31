from turtle import Turtle

class Paddle(Turtle):

            def __init__(self, side):
                super().__init__()
                if side == "r":
                    self.x_pos = 350
                    self.side = "r"
                elif side == "l":
                    self.x_pos = -350
                    self.side = "l"
                self.penup()
                self.goto(self.x_pos, 0)
                self.shape("square")
                self.color("white")
                self.shapesize(stretch_wid=5, stretch_len=1)


# turtle square object. default square size is 20x20

            def move_up(self):
                new_y = self.ycor() + 20
                self.goto(x=self.x_pos, y=new_y)

            def move_down(self):
                new_y = self.ycor() - 20
                self.goto(x=self.x_pos, y=new_y)