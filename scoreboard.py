from turtle import Turtle

class ScoreBoard(Turtle):

        def __init__(self):
            super().__init__()
            self.goto(0, 270)
            self.score_right = 0
            self.score_left = 0
            self.hideturtle()
            self.pencolor("white")
            self.write(arg=f"{self.score_left} : {self.score_left} ", align="center", font=("Arial", 15, "normal"))


        def update(self, side):
            if side == "r":
                self.score_right += 1
            elif side == "l":
                self.score_left += 1
            self.clear()
            self.write(arg=f"{self.score_left} : {self.score_right}", align="center", font=("Arial", 15, "normal"))


        def game_over(self):
            self.penup()
            self.goto(0, 0)
            self.pendown()
            self.pencolor("red")
            self.write(arg=f"GAME OVER ", align="center", font=("Arial", 15, "normal"))