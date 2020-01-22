import os
import random

from code.classes.game import Game
from code.classes.board import Board

def randomize(cars):
    lvl1 = Game('gameboards/Rushhour6x6_1.csv')
    size = lvl1.size
    gameboard_file = lvl1.gameboard_file
    board = Board(size, gameboard_file)
    board.print_board

    steps_dict = {}
    step_count = 1
    while board.won() == False:
        # generate random car + move
        move = random.choice([-2,-1,1,2])
        car = random.choice(cars)

        move_car = board.move_car(cars, car, move)
        move_car

        # increase steps if move is valid
        if move_car is not False:

            steps_dict[step_count] = [car[0],move], board.board
            print(step_count)
            step_count += 1

    print(f"GAME IS WON IN {step_count} STEPS!")
    return steps_dict
