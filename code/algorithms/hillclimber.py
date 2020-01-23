from .randomize import randomize
import numpy



class Hillclimber:

    def __init__(self, board):
        self.board = board


    def load_random(self):
        """
        Returns a dictionary containing all steps and boards per step to a random random solution.
        """
        random_solution = randomize(self.board)

        return random_solution

    def load_goal(self):
        """
        Boolean for when a solution with lesser steps is found.
        """
        random_solution = self.load_random()
        step_count = len(random_solution) + 1
        halfway = round(step_count/2)
        goal = random_solution[halfway][1]
        print("goal:\n", goal)

    def goal_reached(self):
        pass








# def hillclimber(board):
#     print("inside hillclimber algorithms")
#     random0 = randomize(board)
#     # print(random0)
#     step_count = len(random0) + 1
#
#     # retrieve board halfway through the agorithm
#     halfway = round(step_count / 2)
#     print(step_count)
#     print(halfway)
#
#     print(random0[halfway][1])

    # take startpoint, and first half as endpoint
        # While route length is equal to or larger than 25% of the steps
            # randomly make a route from startpoint to endpoint
            # if this route is has less steps than the 25% taken
                # save it as the first 25% of the STEPS
                # break
