from .randomize import randomize
import numpy


def hillclimber(cars):
    print("inside hillclimber algorithms")
    steps = randomize(cars)
    splitzel = split_list(steps, 2)
    print(splitzel)
    amount_of_steps = len(steps)
    #print("steps", steps, "nr_of_steps", amount_of_steps)

    # take the first 50% of the step
    first_half_steps = round(amount_of_steps / 2)
    print(first_half_steps)

    # take startpoint, and first half as endpoint
        # While route length is equal to or larger than 25% of the steps
            # randomly make a route from startpoint to endpoint
            # if this route is has less steps than the 25% taken
                # save it as the first 25% of the STEPS
                # break

def split_list(lst, n):
    splitted = []
    for i in reversed(range(1, n + 1)):
        split_point = len(lst)//i
        splitted.append(lst[:split_point])
        lst = lst[split_point:]
    return splitted
