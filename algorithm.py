import csv

# NOTE: huidige Board class werkt alleen voor eerste bord
# class SlechteGame:
#     def __init__(self):
#         with open("gameboards/Rushhour6x6_1.csv") as csv_file:
#             game = csv.reader(csv_file, delimiter=',')
#             for row in game:
#                 orientation = row[1]
#                 # create list for coordinates for iteration
#                 coordinates = [row[2],row[3]]
#                 length = row[4]
#                 # create car for each row
#                 row[0]=Car(orientation, coordinates, length)
#             self.game = game
#
#         # NOTE: deze moet nog dynamisch gemaakt worden o.b.v. de csv titel
#         self.size = 6


class Game:
    def __init__(self, gameboard_file):
        self.gameboard = self.load_gameboard(gameboard_file)

    def load_gameboard(self, gameboard_file):
        with open(gameboard_file, "r") as in_file:
            reader = csv.DictReader(in_file)
            cars = {}

            for row in reader:
                cars[row['car']] = Car(row['orientation'], row['"x,y"'], row['length'])
                print(row)

class Car:
    def __init__(self, orientation, coordinates, length):
        self.orientation = orientation
        self.coordinates = coordinates
        self.length = length
        # print(f" {self.orientation}, {self.coordinates}, {self.length}")






#
# class Car:
#     def __init__(self, orientation, coordinates, length):
#         self.orientation = orientation
#         self.coordinates = coordinates
#         self.length = length
#         print(f" {self.orientation}, {self.coordinates}, {self.length}")
#
#     def move(self):
#         pass
#         # input: name, orientatie
#
#     def won(self):
#         pass
#         # if rode auto staat op plek 3,6 --> win
#
#     def __str__(self):
#         return(f"{self.name}, {self.orientation}, {self.coordinates}, {self.length}")


# NOTE: Dit weghalen bij het inleveren, aparte "main.py" file maken
if __name__ == "__main__":
    # one = "gameboards/Rushhour6x6_1.csv"
    # two = "gameboards/Rushhour6x6_2.csv"
    # three = "gameboards/Rushhour6x6_3.csv"
    # four = "gameboards/Rushhour9x9_4.csv"
    # five = "gameboards/Rushhour9x9_5.csv"
    # six = "gameboards/Rushhour6x9x9.csv"
    # seven = "gameboards/Rushhour12x12_7.csv"

    # with open("gameboards/Rushhour6x6_1.csv") as csv_file:
    #     game = csv.reader(csv_file, delimiter=',')
    #     for row in game:
    #         name = row[0]
    #         orientation = row[1]
    #         coordinates = row[2]
    #         length = row[3]
    #         Car(name, orientation, coordinates, length)
    Game('gameboards/Rushhour6x6_1.csv')
