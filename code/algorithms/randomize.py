import os, random
import time
from code.classes.game import Game
from code.classes.board import Board

def randomize(board):

    cars = board.cars
    current_board = board.board

    # start the running time of the algorithm
    start_time = time.time()
    steps_list = []

    while board.won(current_board) == False:
        # generate random car + move
        move = random.choice([-2,-1,1,2])
        car = random.choice(cars)
        move_car = board.move_car(cars, car, move)

        # increase steps if move is valid
        if move_car is not False:
            cars = move_car[0]
            current_board = move_car[1]
            steps_list.append([(car[0], move), current_board])

    # Measure the time this function has taken to run
    elapsed_time = round(time.time() - start_time, 4)

    # analyses the results of the board
    board.results(steps_list, elapsed_time)
    
    # Prints all the random steps to the screen
    for z in steps_list:
        board.print_board(cars, z[1])

    return steps_list
