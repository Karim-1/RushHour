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

    # Loads the cars in the board
    randomcar = random.choice(board1.load_cars())
    randommove = random.choice([-1,1])
    loaded_board = board1.load_board()

    # Checks if a particular car can be moved
    move1 = Move(randomcar, randommove, size, loaded_board)
    print(move1.valid_move())

    # Prints the board
    board1.print_board()
