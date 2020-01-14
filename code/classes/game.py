from car import Car
#from board import Board
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
                print(f"Car {car[0]} moved left")
                car[2] = car[2] + move
            else:
                return False 

        if car[1] == "V":
            # check direction to move
            if self.valid_move(car, move):
                print(f"Car {car[0]} moved left")
                car[3] = car[3] + move
            else:
                return False                

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
                mve = move + i + 1
                # check if car stays on the board   
                if (col + mve < 0) or (col + mve + car[4] > self.size):
                    print("false 1")
                    return False
                elif mve < 0:
                    if self.board[row][col + mve] != 'O':
                        print("false 2")
                        return False
                elif mve > 0:
                    if self.board[row][col + car[4] + mve - 1] != 'O':
                        print("false 3")
                        return False

        # check move for vertical cars
        for i in range(abs(move)):
            if orientation == 'V':
                mve = move + i + 1
                print(mve)
                if ((row - mve) < 0) or (row-mve+car[4] > self.size):
                    print("false 4")
                    return False
                elif mve < 0:
                    if self.board[row - mve][col] != 'O':
                        print("false 5")
                        return False
                elif mve > 0:
                    if self.board[row - car[4] - mve + 1][col] != 'O':
                        print("false 6")
                        return False

        print("true")
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
    
    # car_name = lvl1.cars[0][0]
    # orientation = lvl1.cars[0][1]
    # coordinates = [int(lvl1.cars[0][2]), int(lvl1.cars[0][2])]
    # direction = -1
    # print(f"Move to: {direction}")
    # #lvl1.move_car(car_name, orientation, direction)
    # print(f"Car:{car_name}: coordinates:{coordinates}")
    cars = lvl1.load_cars()
    # current_board = Board(6, cars)
    # print("HIER")
    # print(current_board)
    #print(cars[11])
    lvl1.valid_move(cars[9], -1)

