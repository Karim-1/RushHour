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
        if int(filename[8]) == 1:
            self.size = 12
        else:
            self.size = int(filename[8])
        print(self.size)
        self.gameboard_file = gameboard_file



# NOTE: Dit weghalen bij het inleveren, aparte "main.py" file maken
if __name__ == "__main__":

    # initialize first game and board
    lvl1 = Game('../../gameboards/Rushhour6x6_1.csv')
    size = lvl1.size
    gameboard_file = lvl1.gameboard_file
    board1 = Board(size, gameboard_file)


    cars_begin = board1.cars


    # random algorithm:
    """
    steps = 0
    while board1.won() == False:
        # generate random car + move
        move = random.choice([-2,-1,1,2])
        car = random.choice(cars)

        move_car = board1.move_car(car, move)
        move_car

        print(board1.board)
        # increase steps if move is valid
        if move_car is not False:
            steps += 1
            print(steps)

    print(board1.board)
    print(f"GAME IS WON IN {steps} STEPS!")
    """

    from copy import deepcopy
    import queue
    import sys
    import numpy as np

    x = set()
    dict = {}
    q = queue.Queue()

    # place the begin board in queue
    q.put(cars_begin)
    cars = cars_begin

    while not q.empty():
        # states = board
    
        cars = q.get()
        print("QGET",cars)


        for car in cars:
            for step in [x for x in range(-size, size) if x != 0]:
                #print('STATE', state)
                #laat move nieuw board returnen, anders false
                move = board1.move_car(cars, car, step)
                if (move != False) and (str(move[0]) not in x):
                    print("CHECK", car, step)
                    print(move[1])
                    # keuzes (onthou vorige boards & exclude)
                    cars = move[0]
                    print("CORRECT MOVE")
                    #print(car,step)
                    print("CARS", cars)
                    child = deepcopy(cars)
                    dict[str(move[0])] = child
                    x.add(str(cars))
                    q.put(child)

                    #if Board.won(move):
                    for i in reversed(range(size)):
                        print(move[1][2][i])
                        if move[1][2][i] == 'X':
                            print("GOEDGEKEURD")
                            sys.exit()
                            break

                        elif move[1][2][i] == '_':
                            pass

                        else:
                            print("AFGEKEURD")
                            break
                else:
                    print("INVALID MOVE")


        print(q.qsize())
        #print(q.queue)
        print("ALLES\n\n\n\n")
        


    # test with a sequence of cars
    #print(board1.board)
    #board1.move_car(cars[0], -2)
    # print(board1.board)
    # board1.move_car(cars[1], -2)
    # print(board1.board)
    # board1.move_car(cars[2], -1)
    # print(board1.board)
    # board1.move_car(cars[3], -1)
    # # test with a sequence of cars
    # print(board1.board)
    # board1.move_car(cars[5], 3)
    # print(board1.board)
    # board1.move_car(cars[4], -1)
    # print(board1.board)
    # board1.move_car(cars[1], -3)
    # print(board1.board)
    # board1.move_car(cars[0], -3)
    # print(board1.board)
    # board1.move_car(cars[1], 3)
    # print(board1.board)
    # board1.move_car(cars[4], 1)
    # print(board1.board)
    # board1.move_car(cars[5], -2)
    # print(board1.board)
    # board1.move_car(cars[-1], -2)
    # print(board1.board)
