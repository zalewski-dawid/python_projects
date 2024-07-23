#DAWID ZALEWSKI
from turtle import Turtle,Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

#Creating Paddles and Screen


screen=Screen()
screen.title("Pong Game")
screen.setup(width=800,height=600)
screen.bgcolor('black')
screen.listen()

a_paddle=Paddle()
b_paddle=Paddle()

#Creating dash line

dash_cord = [(0,250),(0,200),(0,150),(0,100),(0,50),(0,0),(0,-50),(0,-100),(0,-150),(0,-200),(0,-250)]
for y_c in dash_cord:
    new_dash_line=Turtle()
    new_dash_line.speed("fastest")
    new_dash_line.shapesize(stretch_wid=0.5, stretch_len=0.1)
    new_dash_line.penup()
    new_dash_line.shape("square")
    new_dash_line.color("white")
    new_dash_line.goto(y_c)


ball=Ball()
scoreboard=Scoreboard()
screen.onkeypress(a_paddle.up,"w")
screen.onkeypress(a_paddle.down,"s")
screen.onkeypress(b_paddle.up,"Up")
screen.onkeypress(b_paddle.down,"Down")


game_is_on=True


while game_is_on:
    ball.move_ball()
    # Detect collision with top/bottom wall
    if ball.ycor() < -260 or ball.ycor() > 280:
        ball.sety(ball.ycor())
        ball.setheading(-ball.heading())

    # Detect ball hits paddle
    if ball.distance(a_paddle) < 35 and (ball.heading()>=105 and ball.heading()<=245) :

        ball.ball_paddle_bounce()

    if ball.distance(b_paddle) < 35 and ((ball.heading()>=0 and ball.heading()<=75) or (ball.heading()>=300 and ball.heading()<=360)):
        ball.ball_paddle_bounce()


    #Detect ball hits left/right wall and not paddle

    # left wall
    if ball.xcor()<-370 and ball.distance(a_paddle)>35:
        ball.hideturtle()
        ball.goto(0,0)
        ball.showturtle()
        scoreboard.increase_score_b()
    #right wall
    if ball.xcor()>370 and ball.distance(b_paddle)>35:
        ball.hideturtle()
        ball.goto(0,0)
        ball.showturtle()
        scoreboard.increase_score_a()


screen.exitonclick()