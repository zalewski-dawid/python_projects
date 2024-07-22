from turtle import Screen,Turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from starting_game import StartingGame
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Snake Game")
screen.bgcolor("black")
screen.tracer(0)



snake=Snake()
food=Food()
scoreboard=Scoreboard()

start_game=StartingGame()
start_game.write_message()
game_is_on=False
def enter():
    global game_is_on
    game_is_on= True
    game_loop()
    global start_game
    start_game.hide_t()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.onkey(enter,"Return")

def game_loop():
    global game_is_on
    if game_is_on:
        screen.update()
        time.sleep(0.1)
        snake.move()

        #Detect collision with food
        if snake.head.distance(food)<15:
            food.refresh()
            snake.extend()
            scoreboard.increase_score()
        #Detect collision with wall
        if snake.head.xcor()>295 or snake.head.xcor()<-300 or snake.head.ycor()>300 or snake.head.ycor()<-295:
            game_is_on=False
            scoreboard.printing_game_over()

        #Detect collision with tail
        for segment in snake.segments[1:]:
            if snake.head.distance(segment)<10:
                game_is_on=False
                scoreboard.printing_game_over()
        # Call game_loop again after 10 ms
        screen.ontimer(game_loop, 5)

screen.mainloop()

screen.exitonclick()