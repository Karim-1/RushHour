from car import Car
from board import Board
from move import Move

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

    # Create a string function
    def __repr__(self):
        s=""
        for c in self.cars:
            s+=str(c)
        return s

    # VERANDEREN NAAR BOARD IPV CARS
    def won(self):
        """
        Checks if the red car can drive through the exit of the parking lot.
        If so, the game is won.
        """

        if self.cars[-1][3] == self.size - 1:
            return True
        return False

# NOTE: Dit weghalen bij het inleveren, aparte "main.py" file maken
if __name__ == "__main__":

    # initialize first game and board
    lvl1 = Game('../../gameboards/Rushhour6x6_1.csv')
    size = lvl1.size
    gameboard_file = lvl1.gameboard_file
    board1 = Board(size, gameboard_file)

    # randomcar = random.choice(board1.load_cars())
    # randommove = random.choice([-1,1])
    cars = board1.cars


    # # random algorithm:
    # steps = 0
    # while board1.won() == False:
    #     move = random.choice([-1,1])
    #     car = random.choice(cars)
    #     print(car)
    #
    #     board1.move_car(car, move)
    #
    #     steps += 1
    #
    # print(f"GAME IS WON IN {steps} STEPS! JOEPIE")


    # test with a sequence of cars
    print(board1.board)
    board1.move_car(cars[0], -1)
    print(board1.board)
    board1.move_car(cars[2], -1)
    print(board1.board)
    board1.move_car(cars[6], 1)
    print(board1.board)
