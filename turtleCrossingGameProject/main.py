#DAWID ZALEWSKI
from turtle import Turtle,Screen
from blocks import Blocks
from player import Player
import time
from scoreboard import Scoreboard
import random



screen=Screen()
screen.setup(width=700,height=500)
screen.tracer(0)
blocks=Blocks()
player=Player()
screen.listen()
scoreboard=Scoreboard()
screen.onkeypress(player.move_player,"space")

game_is_on=True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    blocks.create_block()
    blocks.move_blocks()

    #detect collision with block
    for block in blocks.all_blocks:
       if block.distance(player)<18:
        scoreboard.game_over_score()
        game_is_on=False

    #detect player finished level
    if player.is_at_finish_line():
        player.start_pos()
        scoreboard.increase_score()
        #increasing speed depends of level
        blocks.increase_speed()
screen.exitonclick()
