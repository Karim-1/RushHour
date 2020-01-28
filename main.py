from code.classes.board import Board
from code.classes.car import Car
from code.classes.game import Game

from code.algorithms import breadthfirst
from code.algorithms.cut import Cut
from code.algorithms.randomize import randomize
from code.algorithms import random_bfs

from code.helpers.show_results import show_results

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

    # Uncomment line 27-28 to run the random algorithm
    # random_run = randomize(board)
    # show_results(random_run[0], random_run[1], random_run[2], random_run[3])

    # Uncomment line 31-33 to run the Cut algorithm
    # cut = Cut(board)
    # divider = 10
    # cut.run(divider)

    # breadthfirst
    #breadthfirst.breadthfirst(size, board, cars)

    # randomize combined with breadthfirst
    random_bfs.random_bfs(size, board, cars)






    # Try random algorithm
