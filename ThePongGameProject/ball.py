from turtle import Turtle
import random
class Ball(Turtle):
    def __init__(self):
        super().__init__()

        self.shape("circle")
        self.color("yellow")
        self.speed("fast")
        self.penup()
        self.goto(0, random.randint(-220,220))
        randomhead_list=[]
        for i in range(0,65):
            randomhead_list.append(i)
        for i in range(125,245):
            randomhead_list.append(i)
        for i in range(300,360):
            randomhead_list.append(i)

        randomhead=random.choice(randomhead_list)
        self.setheading(randomhead)


    def move_ball(self):
        self.forward(10)

    def ball_paddle_bounce(self):
        self.setheading(180-self.heading())

