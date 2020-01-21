import os
import random

from code.classes.game import Game
from code.classes.board import Board

def randomize(cars):
    lvl1 = Game('gameboards/Rushhour6x6_1.csv')
    size = lvl1.size
    gameboard_file = lvl1.gameboard_file
    board = Board(size, gameboard_file)

    steps = 0
    while board.won() == False:
        # generate random car + move
        move = random.choice([-2,-1,1,2])
        print("move:", move)
        car = random.choice(cars)
        print("car:", car)

        move_car = board.move_car(cars, car, move)

        print("board", board)
        # increase steps if move is valid
        if move_car is not False:
            steps += 1
            print("steps", steps)

    print("board2", board)
    print(f"GAME IS WON IN {steps} STEPS!")
