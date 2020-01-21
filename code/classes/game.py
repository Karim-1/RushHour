from .board import Board

import os
import random

# Creates a class in which the game is played
# With function to check if the game is won

class Game:
    def __init__(self, gameboard_file):

        # retrieve board size from filename of the board
        filename = os.path.basename(gameboard_file)
        if int(filename[8]) == 1:
            self.size = 12
        else:
            self.size = int(filename[8])
        self.gameboard_file = gameboard_file
