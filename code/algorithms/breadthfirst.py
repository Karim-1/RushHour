from copy import deepcopy
import queue
import sys
import numpy as np

from code.classes.game import Game
from code.classes.board import Board


def breadthfirst(cars, size):
    lvl1 = Game('gameboards/Rushhour6x6_1.csv')
    size = lvl1.size
    gameboard_file = lvl1.gameboard_file
    board = Board(size, gameboard_file)

    x = set()
    dict = {}
    q = queue.Queue()

    # place the begin board in queue
    q.put(cars)

    while not q.empty():
        # states = board

        cars = q.get()
        print("QGET",cars)


        for car in cars:
            for step in [x for x in range(-size, size) if x != 0]:
                #print('STATE', state)
                #laat move nieuw board returnen, anders false
                move = board.move_car(cars, car, step)
                # if (move != False) and (str(move[0]) not in x):
                #     print("CHECK", car, step)
                #     print(move[1])
                #     # keuzes (onthou vorige boards & exclude)
                #     cars = move[0]
                #     print("CORRECT MOVE")
                #     #print(car,step)
                #     print("CARS", cars)
                #     child = deepcopy(cars)
                #     dict[str(move[0])] = child
                #     x.add(str(cars))
                #     q.put(child)
                #
                #     #if Board.won(move):
                #     for i in reversed(range(size)):
                #         #print(move[1][2][i])
                #         if move[1][2][i] == 'X':
                #             print("GOEDGEKEURD")
                #             sys.exit()
                #             break
                #
                #         elif move[1][2][i] == '_':
                #             pass
                #
                #         else:
                #             print("AFGEKEURD")
                #             break
                # else:
                #     print("INVALID MOVE")


        print(q.qsize())
        #print(q.queue)
        print("ALLES\n\n\n\n")
