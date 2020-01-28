from code.classes.board import Board
from code.classes.car import Car
from code.classes.game import Game

from code.algorithms import breadthfirst
from code.algorithms.cut import Cut
from code.algorithms.randomize import Randomize
from code.algorithms import random_bfs

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


    # Uncomment line 26-28 to run the random algorithm
    randomize = Randomize(board)
    random_outcome = randomize.run()
    randomize.results(random_outcome)

    # # cut algorithm
    # cut = Cut(board)
    # divider = 10
    # cut.run(divider)

    # breadthfirst
    # breadthfirst.breadthfirst(size, board, cars)

    # randomize combined with breadthfirst
    # random_bfs.random_bfs(size, board, cars)






    # Try random algorithm
