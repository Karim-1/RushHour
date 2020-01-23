from .board import Board

import copy
import sys
import numpy as np

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



# NOTE: Dit weghalen bij het inleveren, aparte "main.py" file maken
if __name__ == "__main__":

    # initialize first game and board
    lvl1 = Game('../../gameboards/Rushhour9x9_4.csv')
    size = lvl1.size
    gameboard_file = lvl1.gameboard_file
    board1 = Board(size, gameboard_file)

    cars = board1.cars.copy()

    # make a set, and add the begin board to it
    history = set()
    history.add(str(cars))

    dict = {}
    queue = []

    # place the begin board in queue
    queue.append(cars)

    while queue:
        test = queue.pop(0)
        old_cars = [x[:] for x in test]
    
        for car in old_cars:
            for step in [x for x in range(-(size-1), size) if x != 0]:
                #print("OLD", old_cars, "CARS", car, step)
                #laat move nieuw board returnen, anders false
                move = Board(9, gameboard_file).move_car(old_cars, car, step)

                if (move != False) and (str(move[0]) not in history):
                    new_cars = move[0].copy()
                    # keuzes (onthou vorige boards & exclude)
                    dict[str(new_cars)] = old_cars
                    history.add(str(new_cars))

                    queue.append(new_cars)

                    #if Board.won(move):
                    for i in reversed(range(size)):
                        if move[1][4][i] == 'X':
                            print("GOEDGEKEURD")
                            k=1
                            print(new_cars)
                            while dict.get(str(new_cars)) != None:
                                new_cars = dict.get(str(new_cars))
                                k=k+1
                                print(new_cars)
                            print("STEPS", k)
                            sys.exit()

                        elif move[1][4][i] != '_':
                            break       
