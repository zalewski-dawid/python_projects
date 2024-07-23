from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.score = 0
        self.color('black')
        self.goto(-240,200)
        self.update_scoreboard()
    def update_scoreboard(self):
        self.write(f"LEVEL: {self.score}",align="center",font=("Arial", 20, "bold"))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def game_over_score(self):
        self.clear()
        self.goto(0, 0)
        self.write(f"GAME OVER !     LEVEL: {self.score}",align="center",font=("Arial", 20, "bold"))