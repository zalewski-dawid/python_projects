from turtle import Turtle
FINISH_LINE=220

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color('black')
        self.shape("turtle")
        self.left(90)
        self.goto(0, -225)
        self.showturtle()

    def move_player(self):
        self.forward(10)

    def start_pos(self):
        self.hideturtle()
        self.goto(0, -225)
        self.showturtle()
    def is_at_finish_line(self):
        if self.ycor()>FINISH_LINE:
            return True
        else:
            return False