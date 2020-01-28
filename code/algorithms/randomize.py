import os, random, time
from code.classes.game import Game
from code.classes.board import Board
from code.helpers.show_results import show_results
from code.helpers.random_move import random_move

def randomize(board):

    start_time = time.time()
    cars = board.cars.copy()
    current_board = board.board.copy()

    steps_list = []

    while board.won(current_board) == False:

        # generate random car + move
        move = random.choice(list(range(-board.size + 1, board.size - 1)))
        car = random.choice(cars)
        move_car = board.move_car(cars, car, move)

        # if move is valid
        if move_car is not False:

            # update cars and board, append move to steps
            cars = move_car[0]
            current_board = move_car[1]
            steps_list.append([(car[0], move), current_board])

    # measure the time this function has taken to run
    elapsed_time = round(time.time() - start_time, 4)

    return board, steps_list, elapsed_time, cars
