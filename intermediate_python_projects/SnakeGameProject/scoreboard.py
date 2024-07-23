from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.penup()
        self.hideturtle()
        self.color("White")
        self.goto(0,280)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score} ", align="center", font=("Arial", 14, "normal"))

    def increase_score(self):

        self.score+=1
        self.clear()
        self.update_scoreboard()

    def printing_game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", align="center", font=("Arial", 14, "normal"))