from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score_a = 0
        self.score_b = 0
        self.goto(0,260)
        self.hideturtle()
        self.color('green')
        self.penup()
        self.update_scoreboard()



    def update_scoreboard(self):
        self.write(f"{self.score_a} | {self.score_b}", align='center', font=('Arial', 24, 'normal'))
    def increase_score_a(self):
        self.score_a +=1
        self.clear()
        self.update_scoreboard()

    def increase_score_b(self):
        self.score_b +=1
        self.clear()
        self.update_scoreboard()