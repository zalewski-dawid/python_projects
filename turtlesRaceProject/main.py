#turtle random speed race. User bet
import turtle
from turtle import Turtle,Screen
import random

screen=Screen()
screen.setup(width=500,height=400)

a_turtle=Turtle()
b_turtle=Turtle()
c_turtle=Turtle()
d_turtle=Turtle()
e_turtle=Turtle()

a_turtle.color("green")
b_turtle.color("blue")
c_turtle.color("yellow")
d_turtle.color("red")
e_turtle.color("black")
a_turtle.shape("turtle")
b_turtle.shape("turtle")
c_turtle.shape("turtle")
d_turtle.shape("turtle")
e_turtle.shape("turtle")

a_turtle.penup()
b_turtle.penup()
c_turtle.penup()
d_turtle.penup()
e_turtle.penup()

a_turtle.goto(-220,150)
b_turtle.goto(-220,75)
c_turtle.goto(-220,0)
d_turtle.goto(-220,-75)
e_turtle.goto(-220,-150)
all_turtles=[a_turtle,b_turtle,c_turtle,d_turtle,e_turtle]


user_bet=screen.textinput(title="Make your bet",prompt="Which turtle will win the race?: ")



if user_bet:
    is_race_on=True

while is_race_on:
    for turtle in all_turtles:
        random_distance=random.randint(0,10)
        turtle.forward(random_distance)
        if turtle.xcor()>230:
            is_race_on=False
            winning_color=turtle.pencolor()
            if winning_color==user_bet:
                print(f"You've won! {winning_color} is the winner !")
            else:
                print(f"You've lost! {winning_color} is the winner !")


screen.exitonclick()