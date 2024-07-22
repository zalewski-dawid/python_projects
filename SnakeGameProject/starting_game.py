from turtle import Turtle,Screen
class StartingGame(Turtle):
    def __init__(self):
        super().__init__()



    def write_message(self):
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 0)
        self.write(f"Press 'ENTER' TO START THE GAME", align="center", font=("Arial", 14, "normal"))
    def hide_t(self):
        self.clear()
        print("dziala")