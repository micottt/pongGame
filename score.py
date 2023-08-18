from turtle import Turtle

alignment = "center"
font = ("Courier", 80, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.left_score = 0
        self.right_score = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.left_score,
                   align=alignment, font=font)
        self.goto(100, 200)
        self.write(self.right_score,
                   align=alignment, font=font)

    def l_point(self):
        self.left_score += 1
        self.update_scoreboard()

    def r_point(self):
        self.right_score += 1
        self.update_scoreboard()