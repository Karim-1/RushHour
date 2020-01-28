from code.classes.board import Board
from code.classes.car import Car
from code.classes.game import Game

"""
main.py

Vanuit deze functie worden alle algoritmes gerunt, en geef je de user de optie om tussen deze te kiezen

"""

from code.algorithms import breadthfirst
from code.algorithms.cut import Cut
from code.algorithms.randomize import randomize
from code.algorithms import random_bfs

from code.helpers.show_results import show_results

import gameboards

if __name__ == "__main__":

    # initialize first game and board
    input_board = input("Please enter the name of the board you want to run (ex: 'gameboards/Rushhour6x6_1.csv'): \n")
    print(input_board)
    if input_board != 'gameboards/Rushhour6x6_1.csv':# or "'gameboards/Rushhour6x6_2.csv'"or "'gameboards/Rushhour6x6_3.csv'" or "'gameboards/Rushhour9x9_4.csv'" or "'gameboards/Rushhour9x9_5.csv'" or "'gameboards/Rushhour9x9_6.csv'" or "'gameboards/Rushhour12x12_7.csv'":
        print("You entered an invalid name")
        sys.exit()

    lvl1 = Game(input_board)
    size = lvl1.size
    gameboard_file = lvl1.gameboard_file
    board = Board(size, gameboard_file)
    cars = board.cars

    # gives user the decision to run an algorithm
    algorithm = input("which algorithm would you like to run? \n 1) press 1 for randomize \n 2) press 2 for the cut algorithm \n 3) press 3 for best first search \n 4) press 4 for random BFS \n")
    if algorithm == '1':

        # line 28-29 run the random algorithm
        random_run = randomize(board)
        show_results(random_run[0], random_run[1], random_run[2], random_run[3])

    elif algorithm == '2':

        # line 33-35 run the Cut algorithm
        divide = False

        while divide == False:
            divider = int(input("Please enter an integer by which you want to divide a random solution for this algorithm (nr between 2 and 100): \n"))

            if (divider >= 2) and (divider <= 100):
                divide = True

        print("Algorithm is running row, please wait .....")
        cut = Cut(board)
        cut.run(divider)

    elif algorithm == '3':

        # line 50 runs the breadthfirst algorithm
        breadthfirst.breadthfirst(size, board, cars)

    elif algorithm == '4':

        # Line 54 runs the randomize combined with breadthfirst
        random_bfs.random_bfs(size, board, cars)

    else:
        print("NO such algorithm in our code.")
