import os
import random

from code.classes.game import Game
from code.classes.board import Board

def randomize(board):

    cars = board.cars

    steps_dict = {}
    steps_count = 1

    while board.won() == False:
        # generate random car + move
        move = random.choice([-2,-1,1,2])
        car = random.choice(cars)


        move_car = board.move_car(cars, car, move)
        move_car

        # increase steps if move is valid
        if move_car is not False:

            steps_dict[steps_count] = [car[0],move], board.board
            steps_count += 1

    print(f"GAME IS WON IN {steps_count} STEPS!")
    return steps_dict
