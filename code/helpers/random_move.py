import random

def random_move(size, cars, board):
    """
    Moves random car.
    """

    # generate random car + move
    move = random.choice(list(range(-size + 1, size - 1)))
    car = random.choice(cars)

    move_car = board.move_car(cars, car, move)
    # increase steps if move is valid
    if move_car is not False:
        cars = move_car[0]
        board = move_car[1]
    return cars, board, (car[0], move)
