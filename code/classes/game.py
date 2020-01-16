from car import Car
from board import Board

import os
import random

# Creates a class in which the game is played
# With function to check if the game is won

class Game:
    def __init__(self, gameboard_file):

        # retrieve board size from filename of the board
        filename = os.path.basename(gameboard_file)
        self.size = int(filename[8])
        self.gameboard_file = gameboard_file



# NOTE: Dit weghalen bij het inleveren, aparte "main.py" file maken
if __name__ == "__main__":

    # initialize first game and board
    lvl1 = Game('../../gameboards/Rushhour6x6_1.csv')
    size = lvl1.size
    gameboard_file = lvl1.gameboard_file
    board1 = Board(size, gameboard_file)


    cars = board1.cars


    # random algorithm:
    steps = 0
    while board1.won() == False:
        # generate random car + move
        move = random.choice([-1,1])
        car = random.choice(cars)

        # move car
        move_car = board1.move_car(car, move)
        move_car

        # increase steps if move is valid
        if move_car is True:
            steps += 1
            print(steps)

    print(board1.board)
    print(f"GAME IS WON IN {steps} STEPS!")


    # # test with a sequence of cars
    # print(board1.board)
    # board1.move_car(cars[0], -1)
    # print(board1.board)
    # board1.move_car(cars[2], -1)
    # print(board1.board)
    # board1.move_car(cars[6], 1)
    # print(board1.board)
    # board1.move_car(cars[6], 1)
    # print(board1.board)
    # board1.move_car(cars[11], -1)
    # print(board1.board)
    # board1.move_car(cars[9], -1)
    # print(board1.board)
    # board1.move_car(cars[8], -1)
    # print(board1.board)

    # test for won()
    # board1.won()
