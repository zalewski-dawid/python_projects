from turtle import Turtle
import random
COLORS = ["red", "green", "yellow", "blue", "magenta", "cyan", "pink"]
levels_dic={
    "1" : "slowest",
    "2" : "slow",
    "3" : "normal",
    "4" : "fast",
    "5" : "fastest",
}
speed_value=5
class Blocks:
    def __init__(self):
        self.all_blocks=[]

    def create_block(self):
        rand_num=random.randint(1,5)
        if rand_num == 1:
            new_block=Turtle("square")
            new_block.shapesize(stretch_len=2, stretch_wid=1)
            new_block.penup()
            random_color = random.choice(COLORS)
            new_block.color(random_color)
            random_y=random.randint(-200, 250)
            new_block.goto(380,random_y)
            self.all_blocks.append(new_block)
    def move_blocks(self):
        for block in self.all_blocks:
            block.backward(speed_value)

    def increase_speed(self):
        global speed_value
        speed_value += 2
