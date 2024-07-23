from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.color("green")
        self.speed("fastest")
        random.x=random.randint(-270,270)
        random.y=random.randint(-270,270)
        self.goto(random.x,random.y)
        self.refresh()
    def refresh(self):
        random.x = random.randint(-270, 270)
        random.y = random.randint(-270, 270)
        self.goto(random.x, random.y)