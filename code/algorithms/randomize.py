import os
import random

from code.classes.game import Game
from code.classes.board import Board

def randomize(cars):
    lvl1 = Game('gameboards/Rushhour6x6_1.csv')
    size = lvl1.size
    gameboard_file = lvl1.gameboard_file
    board = Board(size, gameboard_file)

    print(board.board)
    steps = {}
    steps_count = 0
    while board.won() == False:
        # generate random car + move
        move = random.choice(list(range(-board.size,board.size)))
        car = random.choice(cars)

        # move a car
        move_car = board.move_car(cars, car, move)
        move_car

        # increase steps if move is valid
        if move_car is not False:
            steps_count += 1

            # save steps including the current board in steps dictionary
            steps[steps_count] = [car[0],move], board.board



    print(f"GAME IS WON IN {steps_count} STEPS!")
    return [steps, steps_count]
