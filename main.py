from code.classes.game import Game
from code.classes.board import Board
from code.classes.car import Car

from code.algorithms import randomize
from code.algorithms import breadthfirst

import gameboards

if __name__ == "__main__":

    # initialize first game and board
    lvl1 = Game('gameboards/Rushhour6x6_1.csv')
    size = lvl1.size
    gameboard_file = lvl1.gameboard_file
    board = Board(size, gameboard_file)
    cars = board.cars
    print(cars)
    breadthfirst.breadthfirst(cars, size)
    print("go in randomize")
    randomize.randomize(cars)
    # Try random algorithm



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
