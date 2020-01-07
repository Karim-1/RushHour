import csv

class Board(game):


    def __init__(self):
        with open("gameboards/Rushhour6x6_1.csv") as csv_file:
            game = csv.reader(csv_file, delimiter=',')
            for row in game:
                print(", ".join(row))

        self.game = game
        self.size = 6

class Car(car, board):
    def __init__(self):
        self.car = car
        self.orientation = H
        self.position = "2,6"
        self.length = 2
        self.board = board

    def move(self):
        pass

    def won(self):
        # if rode auto staat op plek 3,6 --> win


if __name__ == "__main__":
    one = "gameboards/Rushhour6x6_1.csv"
    two = "gameboards/Rushhour6x6_2.csv"
    three = "gameboards/Rushhour6x6_3.csv"
    four = "gameboards/Rushhour9x9_4.csv"
    five = "gameboards/Rushhour9x9_5.csv"
    six = "gameboards/Rushhour6x9x9.csv"
    seven = "gameboards/Rushhour12x12_7.csv"

    #ask user which game should be played
    # print("Which game should be played?")
    # input = input()
    with open("gameboards/Rushhour6x6_1.csv") as csv_file:
        game = csv.reader(csv_file, delimiter=',')
        for row in game:
            print(", ".join(row))
