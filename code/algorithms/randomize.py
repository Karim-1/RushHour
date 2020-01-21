import os
import random

from code.classes.game import Game
from code.classes.board import Board

def randomize(cars):
    lvl1 = Game('gameboards/Rushhour6x6_1.csv')
    size = lvl1.size
    gameboard_file = lvl1.gameboard_file
    board = Board(size, gameboard_file)

    steps = []
    while board.won() == False:
        # generate random car + move
        move = random.choice([-2,-1,1,2])
        car = random.choice(cars)

        move_car = board.move_car(cars, car, move)
        move_car
        # increase steps if move is valid
        if move_car is not False:
            steps.append([car[0],move])
            print("steps", len(steps))
            print(board.board)

    print(f"GAME IS WON IN {len(steps)} STEPS!")
    return steps
