import os, time
from code.classes.game import Game
from code.classes.board import Board
from code.helpers.show_results import show_results
from code.helpers.random_move import random_move

class Randomize:
    """
    This class moves cars at random untill a solution has been found.
    """

    def __init__(self, board):
        self.board = board
        self.cars = board.cars

    def run(self):
        """
        Runs the random algorithm.
        """

        cars = self.board.cars.copy()
        current_board = self.board.board.copy()

        # start the running time of the algorithm
        start_time = time.time()
        steps_list = []

        while self.board.won(current_board) == False:

            randomized_move = random_move(self.board.size, cars, current_board)
            steps_list.append((randomized_move[2], randomized_move[1]))
            cars = randomized_move[0]
            print(current_board)

        # measure the time this function has taken to run
        elapsed_time = round(time.time() - start_time, 4)


        return steps_list, elapsed_time, cars

    def results(self, outcome):
        """
        Shows the running time, amount of steps and displays all the boards.
        """
        show_results(self.board, outcome[0], outcome[1], outcome[2])
