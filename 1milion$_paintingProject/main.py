#import colorgram
#colors=colorgram.extract('image.jpeg',30)
#rgb_colors=[]

#for color in colors:
 #   r=color.rgb.r
  #  g=color.rgb.g
   # b=color.rgb.b
    #new_color=(r,g,b)
   # rgb_colors.append(new_color)

from turtle import Turtle,Screen
import turtle as turtle_module
import random

turtle_module.colormode(255)
timmy=Turtle()
screen=Screen()


color_list=[(252, 250, 247), (253, 247, 249), (237, 251, 245), (249, 228, 17), (213, 13, 9), (198, 12, 35), (231, 228, 5), (197, 69, 20), (33, 90, 188), (43, 212, 71), (234, 148, 40), (33, 30, 152), (16, 22, 55), (66, 9, 49), (240, 245, 251), (244, 39, 149), (65, 202, 229), (14, 205, 222), (63, 21, 10), (224, 19, 111), (229, 165, 8), (15, 154, 22), (245, 58, 16), (98, 75, 9), (248, 11, 9), (222, 140, 203), (68, 240, 161), (10, 97, 62), (5, 38, 33), (68, 219, 155)]

timmy.hideturtle()
timmy.penup()
timmy.setheading(225)
timmy.forward(300)
timmy.setheading(0)
timmy.pendown()

def draw_dots():
    for i in range(10):

        for i in range(10):
            timmy.dot(20, random.choice(color_list))
            timmy.penup()
            timmy.forward(50)
            timmy.pendown()


        timmy.penup()
        timmy.left(90)
        timmy.forward(50)
        timmy.left(90)
        timmy.forward(500)
        timmy.left(90)
        timmy.left(90)
        timmy.pendown()

draw_dots()



screen.exitonclick()