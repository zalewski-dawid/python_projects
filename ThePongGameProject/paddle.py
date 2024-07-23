from turtle import Turtle
coordinates=[(-360,0),(360,0)]
paddle_colors=['red','blue']
n=0
class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.paddle_features()
        global n
        self.goto(coordinates[n])
        self.color(paddle_colors[n])
        n+=1

    def paddle_features(self):
        self.penup()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=4, stretch_len=0.5)
        self.speed(0)

    def up(self):
        new_y=self.ycor()+10
        if new_y<280:
            self.goto(self.xcor(),new_y)

    def down(self):
        new_y = self.ycor() -10
        if new_y > -280:
            self.goto(self.xcor(), new_y)



