from .randomize import randomize


def hillclimber(cars):
    print("inside hillclimber algorithms")
    steps = randomize(cars)
    amount_of_steps = len(steps)
    print("steps", steps, "nr_of_steps", amount_of_steps)

    # take the first 25% of the steps
        # take startpoint, and endpoint
        # While route length is equal to or larger than 25% of the steps
            # randomly make a route from startpoint to endpoint
            # if this route is has less steps than the 25% taken
                # save it as the first 25% of the STEPS
                # break
