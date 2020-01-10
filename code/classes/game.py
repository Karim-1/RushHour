from car import Car
from board import Board
import csv
import os
import random

# Mentorgesprek notes: class car (x,y, orientatie, length, name)
# class board
# `classs game (car_list, board)
# functie Move_car(iD, direction), als deze wordt aangeroepen, zorg dan dat je game veranderds
# functie Is_win
# functie Is_emptyss
# Mathplotlib gebruiken om vierkantjes te maken om bord te visualiseren `9makkelijker dan je denkt`
# de algorithmes pakken move_cvar


class Game:
    def __init__(self, gameboard_file):
        # retrieve board size from filename
        filename = os.path.basename(gameboard_file)
        size = int(filename[8])

        self.size = size
        self.gameboard_file = gameboard_file
        self.cars = self.load_cars()

    def load_cars(self):
        """
        Loads all cars into the game
        """
        # read through csv gameboard file
        with open(self.gameboard_file, "r") as in_file:
            reader = csv.DictReader(in_file, skipinitialspace=True)
            cars = []

            # create car for each row
            for row in reader:
                coordinates = row['x,y'].split(",")
                car = Car(row['car'], row['orientation'], int(coordinates[0]), int(coordinates[1]), row['length'])
                cars.append(car.info)
            return cars

    def move_car(self, car_name, orientation, direction):
        # check orientation to decide in which way to move
        if orientation == "H":
            # check direction to move
            if direction == -1:
                print(f"Car {car_name} moved left")
                for car in self.cars:
                    # search car_name
                    if car[0] == car_name:
                        print("oude auto:", car)
                        # move car if move is valid
                        self.valid_move(car_name)
                        if self.valid_move(car_name) == True:
                            car[2] = car[2] - 1
                            print("nieuwe auto:", car)
                        else:
                            print("invalid move")

            if direction == 1:
                print(f"Car {car_name} moved right")
        elif orientation =="V":
            if direction == -1:
                print(f"Car {car_name} moved up")
            if direction == 1:
                print(f"Car {car_name} moved down")
        else:
            return False


    def valid_move(self, car_name):
        # check if car is still on the board
        print(car_name)
        print(self.cars[0][0])
        for car in self.cars:
            if car[0] == car_name:
                print("check",car[2], car[3])
                if car[2] or car[3] < 1:
                    return False
                    print("FALSE1")
                if car[2] or car[3] > self.size:
                    return False
                    print("FALSE2")
        print("TRUE")
        return True


    def random_car(self):
        # choose random car
        return random.choice(self.cars)

    def random_move(self):
        # list with back- or forward move
        move = [1,-1]
        # return random move
        return random.choice(move)

    def won(self):
        # if red car reaches the right side of the board, game is won
        if self.cars[-1][3] == self.size - 1:
            return True
        return False



    # in string method functie maken die bord simuleert
    def __repr__(self):
        s=""
        for c in self.cars:
            s+=str(c)
        return s


# NOTE: Dit weghalen bij het inleveren, aparte "main.py" file maken
if __name__ == "__main__":
    lvl1 = Game('../../gameboards/Rushhour6x6_1.csv')
    car_name = lvl1.cars[0][0]
    orientation = lvl1.cars[0][1]
    coordinates = [int(lvl1.cars[0][2]), int(lvl1.cars[0][2])]
    direction = -1
    print(f"Move to: {direction}")
    lvl1.move_car(car_name, orientation, direction)
    print(f"Car:{car_name}: coordinates:{coordinates}")
    cars = lvl1.load_cars()
    current_board = Board(6, cars)
    #print(current_board)
