
from .randomize import randomize
import numpy, random, time, copy


class Cut:
    """
    This algorithm replaces parts of the steps to a solution with a smaller amount of steps.
    """

    def __init__(self, board):
        self.board = board
        self.cars = board.cars


    def run(self):
        """
        Runs the algorithm.
        """

        # generate random solution
        solution = randomize(self.board)
        # make copies of board
        board = self.board.board.copy()

        cars = self.cars

        counter = 0
        attempts = 0
        new_steps = []

        # cut steps into 10
        cut_steps = round(len(solution)/10)
        print("cut_steps:", cut_steps)

        # create path for every 20 steps
        for i in (range(cut_steps, len(solution), cut_steps)):

            # cut_goal = solution[i]
            goal_board = solution[i][1]

            # create starting board for while loop
            start_board = solution[i - 20][1]
            current_board = board.copy

            steps = []
            attempts = 0

            while self.goal_reached(goal_board, current_board) == False:

                move = self.random_move(cars, current_board)
                cars = move[0]
                current_board = move[1]

                steps.append(move[2])

                counter += 1

                # if the goal hasn't been reached in 20 steps
                if counter == cut_steps:

                    # reset counter, list with steps and board
                    counter = 0
                    steps = []
                    current_board = start_board

                    attempts += 1
                    # print(f"Attempt {attempts}")


                if attempts == 1000:
                    print("no solution found in 1000 steps, keeping old steps")
                    for j in (range(i-20, i)):
                        steps.append(solution[j][0])
                    break
            print("new route found in", len(steps)," steps")
            new_steps.extend(steps)


        print("old solution:", len(solution), "steps")
        # delete old path, add new path
        solution = new_steps
        print("new solution:", len(solution), "steps")

    def goal_reached(self, goal, board):
        """
        Returns true if the board matches the goal board.
        """
        if board == goal:
            return True
        return False

    def random_move(self, cars, board):
        """
        Moves random car.
        """
        # generate random car + move
        move = random.choice([-2,-1,1,2])
        car = random.choice(cars)

        move_car = self.board.move_car(cars, car, move)
        # increase steps if move is valid
        if move_car is not False:
            cars = move_car[0]
            board = move_car[1]
        return cars, board, (car[0], move)
