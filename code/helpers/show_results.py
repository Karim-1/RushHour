def show_results(board, steps, elapsed_time, cars):
    """
    shows the step and running time results of algorithms

    """
    # Adds one to the complete amount of steps, since the car also needs to ride out of the parking
    steps_length = len(steps) + 1
    print("\nsteps:       ", steps_length, "moves.")
    print("running time:", elapsed_time, "seconds.")

    # Prints all the random steps to the screen
    for z in steps:
        board.print_board(cars, z[1])
