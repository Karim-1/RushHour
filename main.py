from code.classes.board import Board
from code.classes.car import Car
from code.classes.game import Game

from code.algorithms import breadthfirst
from code.algorithms.hillclimber import Hillclimber
from code.algorithms import randomize

# from code.algorithms import breadthfirst
# from code.algorith

import gameboards

if __name__ == "__main__":

    # initialize first game and board
    lvl1 = Game('gameboards/Rushhour6x6_1.csv')
    size = lvl1.size
    gameboard_file = lvl1.gameboard_file
    board = Board(size, gameboard_file)
    cars = board.cars


    # randomize
    # randomize.randomize(board)

    # hillclimber
    hillclimber = Hillclimber(board)
    hillclimber.win_condition()



    # # breadthfirst
    # breadthfirst.breadthfirst(cars, size)

    # Try random algorithm
