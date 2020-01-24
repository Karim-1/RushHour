import os
import random

from code.classes.game import Game
from code.classes.board import Board

def randomize(board):

    cars = board.cars
    current_board = board.board

    steps_dict = {}
    steps_count = 1

    while board.won(current_board) == False:
        # generate random car + move
        move = random.choice([-2,-1,1,2])
        car = random.choice(cars)



        move_car = board.move_car(cars, car, move)

        # increase steps if move is valid
        if move_car is not False:
            cars = move_car[0]
            current_board = move_car[1]
            board.print_board(cars, current_board)
            steps_dict[steps_count] = [car[0],move], current_board
            steps_count += 1


    print(f"GAME IS WON IN {steps_count} STEPS!")
    return steps_dict
