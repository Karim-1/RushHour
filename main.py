from code.classes.board import Board
from code.classes.car import Car
from code.classes.game import Game

from code.algorithms import breadthfirst
from code.algorithms.cut import Cut
from code.algorithms import randomize
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


    # randomize
    # randomize.randomize(board)

    # cut algorithm
    cut = Cut(board)
    print("cut")
    cut.run()

    # breadthfirst
    # breadthfirst.breadthfirst(size, board, cars)

    # randomize combined with breadthfirst
    # random_bfs.random_bfs(size, board, cars)






    # Try random algorithm
