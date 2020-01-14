import random

from game import Game


def move_cars(game):
    car = random_car(game.cars)
    move = random_move()
    print (f"Car: {car[0]}\nMove: {move}")
    Game.move_car(car, move)
    print(Game.board)


def random_car(cars):
    """
    returns random car from list
    """
    return random.choice(cars)

def random_move():
    """
    returns random move from list
    """
    move = [1,-1]
    # return random move
    return random.choice(move)


def won():
    """
    returns True when the red car reaches the right side of the board
    """
    # if red car reaches the right side of the board, game is won
    if Game.cars[-1][3] == Game.size - 1:
        return True
    return False


if __name__ == "__main__":
    lvl1 = Game('../../gameboards/Rushhour6x6_1.csv')
    move_cars(lvl1)
