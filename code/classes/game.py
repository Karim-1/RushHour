from car import Car

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
        self.board = self.load_board()
        print(self.board)

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
                # split x,y column in two separatre list elements
                coordinates = row['x,y'].split(",")
                # append each row as a new car in a list
                car = Car(row['car'], row['orientation'], int(coordinates[0]), int(coordinates[1]), int(row['length']))
                cars.append(car.info)
            return cars
            
    def load_board(self):
        """
        Loads default empty board.
        """
        # make a list inside of a list
        board = [['O' for g in range(self.size)] for h in range(self.size)]

        # loop over all x-coordinates
        for x in range(self.size):

            # loop over all y-coordinates
            for y in range(self.size):

                # loop over all cars
                for car in self.cars:

                    # check for cars at the current coordinate
                    if int(car[2]) == (y+1) and int(car[3]) == (x+1):
                        if car[1]=='H':

                            # loop over length of car
                            for i in range(int(car[4])):
                                # write the name of the car at the correct places
                                board[(self.size-(x+1))][(y+i)]=car[0]

                        # same but for vertically oriented cars
                        if car[1]=='V':
                            for i in range(int(car[4])):
                                board[(self.size-(x+i+1))][(y)]=car[0]
        return board

    def move_car(self, car, move):
        # check orientation to decide in which way to move
        if car[1] == "H":
            # check direction to move
            if self.valid_move(car, move):
                if move < 0:
                    print(f"Car {car[0]} moved left")
                if move > 0:
                    print(f"Car {car[0]} moved right")
                car[2] = car[2] + move
            else:
                return False

        if car[1] == "V":
            # check direction to move
            if self.valid_move(car, move):
                if move < 0:
                    print(f"Car {car[0]} moved down")
                if move > 0:
                    print(f"Car {car[0]} moved up")
                car[3] = car[3] + move
            else:
                return False
        print(car)

    def coord_array(self, x, y):
        """
        Convert coordinates to correct array places.
        """
        x = x - 1
        y = self.size - y
        return [y,x]

    def valid_move(self, car, move):
        # save x and y coordinates
        row = self.coord_array(car[2], car[3])[0]
        col = self.coord_array(car[2], car[3])[1]
        orientation = car[1]

        # check move for horizontal cars
        if orientation == 'H':
            for i in range(abs(move)):
                steps = move + i
                # check if car stays on the board
                if (col + steps < 0) or (col + steps + car[4] > self.size):
                    # print("Car out of bounds")
                    return False
                elif steps < 0:
                    if self.board[row][col + steps] != 'O':
                        # print("Can't move left")
                        return False
                elif steps > 0:
                    if self.board[row][col + car[4] + steps - 1] != 'O':
                        # print("Can't move right")
                        return False

        # check move for vertical cars
        for i in range(abs(move)):
            if orientation == 'V':
                steps = move + i
                if ((row - steps) < 0) or (row-steps+car[4] > self.size):
                    # print("Car out of bounds")
                    return False
                elif steps < 0:
                    if self.board[row - steps][col] != 'O':
                        # print("Can't move down")
                        return False
                elif steps > 0:
                    if self.board[row - car[4] - steps + 1][col] != 'O':
                        # print("Can't move up")
                        return False

        # print("Valid move")
        return True


    # in string method functie maken die bord simuleert
    def __repr__(self):
        s=""
        for c in self.cars:
            s+=str(c)
        return s

    def won(self):
        """
        returns True when car "x" reaches the right side of the board
        """
        # if red car reaches the right side of the board, game is won
        if self.cars[-1][3] == self.size - 1:
            return True
        return False


# NOTE: Dit weghalen bij het inleveren, aparte "main.py" file maken
if __name__ == "__main__":
    lvl1 = Game('../../gameboards/Rushhour6x6_1.csv')

    # car_name = lvl1.cars[0][0]
    # orientation = lvl1.cars[0][1]
    # coordinates = [int(lvl1.cars[0][2]), int(lvl1.cars[0][2])]
    # direction = -1
    # print(f"Move to: {direction}")
    # #lvl1.move_car(car_name, orientation, direction)
    # print(f"Car:{car_name}: coordinates:{coordinates}")
    cars = lvl1.load_cars()
    randomcar = random.choice(lvl1.load_cars())
    randommove = random.choice([-1,1])
    # print("Car:", randomcar[0])
    # print("Move:", randommove)
    lvl1.move_car(cars[0],-1)
    print(lvl1.board)
    counter = 0
    # while lvl1.won()== False:
    #     print(counter,":")
    #     print(lvl1.board)
    #     lvl1.move_car(randomcar,randommove)
    #     counter+=1
