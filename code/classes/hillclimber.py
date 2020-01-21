from game import Game


class Hillclimber(Board):
    """
    The hillclimber class improves parts of the random algorithm.
    This is done by cutting a part of the steps and replacing it with a faster solution.
    """

    def __init__(self):
        pass

    def run(self):
        steps = []
        while Board.won() == False:
            # generate random car + move
            car = random.choice(cars)
            move = random.choice([-3,-2,-1,1,2,3])

            move_car = board1.move_car(car, move)
            move_car

            # increase steps if move is valid
            if move_car is not False:
                steps.append([car,move])
                print(len(steps))

        print(Board.board)

    if __name__ == "__main__":
        lvl1 = Game('../../gameboards/Rushhour6x6_1.csv')
        size = lvl1.size
        gameboard_file = lvl1.gameboard_file
        board1 = Board(size, gameboard_file)

        hillclimber = Hillclimber(board1).run()
