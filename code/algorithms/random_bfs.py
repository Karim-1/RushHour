import sys
import os, random

from code.classes.board import Board


def random_bfs(size, board, cars):

    current_board = board.board

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
            steps_list.append(cars)

    print(f"GAME IS WON IN {len(steps_list)} STEPS!")
    print(steps_list)


    cars = steps_list[-4]

    # make a set, and add the car information of the beginboard to it
    history = set()
    history.add(str(cars))

    # make an empty dictionary, this wil later be used to save parent-child relationships
    dict = {}

    # make list that will function as queue with the car information of the beginboard as starting node
    queue = [cars]

    # start a loop that only ends if all possible states are generated
    while queue:

        # get the first node in the queue, the algorithm reads horizontally
        next_node = queue.pop(0)

        # make a deepcopy of the car information of the parent-node
        old_cars = [x[:] for x in next_node]


        # loop over all cars, and their current information (coordinates)
        for car in old_cars:

            # loop over all possible steps on the board, exclude 0 because it is useless
            for step in [x for x in range(-(size-1), size) if x != 0]:

                # execute move_car function from board.py, returns False if the move is invalid, otherwise: new car information & board
                move = board.move_car(old_cars, car, step)

                # check if move is valid, and if the exact same car information is not already in the tree
                if (move != False) and (str(move[0]) not in history):

                    # add the new car information (returned by move) to the dictionary with the old car information and the move as value
                    new_cars = move[0]
                    dict[str(new_cars)] = [old_cars, [car[0], step]]

                    # add the new car information to the history of tried nodes
                    history.add(str(new_cars))

                    # create the new node in the queue
                    queue.append(new_cars)

                    # check if the current board is the end condition with won function from board.py
                    new_board = move[1]

                    if board.won(new_board):

                        # make a list that will collect all the moves in the winning solution
                        move_list=[]
                        board_list = []

                        # start loop that ends if the node has no parent in the dictionary
                        while dict.get(str(new_cars)) != None:

                            # generating and printing all the correct boards
                            current_board = board.load_board(new_cars)
                            board_list.append([new_cars, current_board])


                            # get the previous car information and the move from dictionary
                            move = dict.get(str(new_cars))[1]
                            new_cars = dict.get(str(new_cars))[0]

                            # add all the necesarry moves to a list
                            move_list.append(move)

                        # iterate over all moves and write them to a csv file using write_output function
                        for s in reversed(move_list):
                            board.write_output(s[0], s[1])

                        # for z in reversed(board_list):
                        #     board.print_board(z[0], z[1])