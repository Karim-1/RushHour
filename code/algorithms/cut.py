from .randomize import randomize
from code.helpers.show_results import show_results
import numpy, random, time, copy

"""
    cut.py
    
    This algorithm cuts up a random solution in 10 equal parts
    and tries to find a random faster path for each part.
    After 1000 attempts it keeps the old path.
"""

class Cut:

    def __init__(self, board):
        self.board = board
        self.cars = board.cars


    def run(self, divider):
        """
        Runs the algorithm.
        """

        start_time = time.time()

        # generate random solution
        solution = randomize(self.board)[1]

        # make copy of board and cars
        board = self.board.board.copy()
        cars = self.cars.copy()

        counter = 0
        attempts = 0
        new_solution = []

        # cut steps into parts
        cut_steps = round(len(solution)/divider)

        # create path for every part
        for i in (range(cut_steps, len(solution), cut_steps)):

            # create board
            goal_board = solution[i][1]

            # create starting board for while loop
            start_board = solution[i - 20][1]
            current_board = board.copy

            steps = []
            attempts = 0

            while current_board != goal_board:

                # move random car
                move = self.random_move(cars, current_board)

                # update cars, board and steps
                cars = move[0]
                current_board = move[1]
                steps.append((move[2], current_board))

                counter += 1

                # if the goal hasn't been reached within cut steps
                if counter == cut_steps:

                    # reset list with steps, counter and board
                    steps = []
                    counter = 0
                    current_board = start_board

                    attempts += 1
                if attempts == 1000:

                    # keep old steps from solution
                    for j in (range(i-cut_steps, i)):
                        steps.append((solution[j][0], solution[j][1]))
                    break

            # add steps to new solution
            new_solution.extend(steps)

        print("old solution:", len(solution))
        print("new solution:", len(new_solution) + 1)

        # calculate the elapsed start_time
        elapsed_time = round(time.time() - start_time, 4)
        # prints the amount of steps, elapsed time and all the boards to the screen
        show_results(self.board, new_solution, elapsed_time, cars)

        return steps


    def random_move(self, cars, board):
        """
        Moves random car.
        """

        # generate random car + move
        move = random.choice(list(range(-self.board.size + 1, self.board.size - 1)))
        car = random.choice(cars)

        move_car = self.board.move_car(cars, car, move)
        # increase steps if move is valid
        if move_car is not False:
            cars = move_car[0]
            board = move_car[1]
        return cars, board, (car[0], move)
