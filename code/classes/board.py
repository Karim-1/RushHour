# these imports are for plotting the board
from matplotlib import pyplot as plt
from matplotlib import colors
import csv
import matplotlib as mpl

from .car import Car

import os

class Board:
    """
    This class represents the game board and allows for board updates based on car moves.
    """

    def __init__(self, size, gameboard_file):
        """
        Intialize board parameters.
        """

        self.size = size
        self.gameboard_file = gameboard_file
        self.cars = self.load_cars()
        self.board = self.load_board(self.cars)

        with open('output.csv', mode='w') as output:
            output_writer = csv.writer(output, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            output_writer.writerow(['Car', 'Move'])

    def load_cars(self):
        """
        Loads all cars into the game.
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

    def load_board(self, cars):
        """
        Loads default empty board.
        """
        # create empty matrix to represent board
        board = [['_' for g in range(self.size)] for h in range(self.size)]

        # loop over all x-coordinates
        for x in range(self.size):

            # loop over all y-coordinates
            for y in range(self.size):

                # loop over all cars
                for car in cars:

                    if car[2] == '_' or car[3] == '_':

                        row = self.convert(int(car[2]), int(car[3]))[0]
                        col = self.convert(int(car[2]), (car[3]))[1]

                        # check for cars at the current coordinate
                        if col == y and row == x:

                            # loop over length of horizontal car
                            if car[1]=='H':
                                for i in range((int(car[4]))):
                                    # write the car name
                                    board[row][col+i]=car[0]

                            # repeat for vertical cars
                            if car[1]=='V':
                                for i in range((int(car[4]))):
                                    board[row-i][col]=car[0]
        return board


    def print_board(self):
        # Make dict with form {A: number}
        dict = {}
        for i in range(len(self.cars)):
                # generate for every car a number between 0 and 1
                j=i+1
                dict[self.cars[i][0]] = (1/len(self.cars))*j

        # iterate over the board
        for i in range(self.size):
            for j in range(self.size):
                # if the place is empty, set 0
                if self.board[i][j] == '_':
                    self.board[i][j]=0
                # if car is red, set 1
                elif self.board[i][j] == 'X':
                    self.board[i][j] = 1
                # else, set to value as calculated above
                else:
                    self.board[i][j] = dict[self.board[i][j]]

        # list of possible colors, ranging from grey to red
        cmap = colors.ListedColormap(['white','yellow', 'orange', 'green', 'purple', 'lightcoral', 'lightcyan', 'aquamarine', 'mediumspringgreen', 'fuchsia', 'mediumslateblue', 'darkviolet', 'dodgerblue', 'pink', 'goldenrod', 'navajowhite', 'mediumpurple', 'olivedrab', 'teal', 'palevioletred', 'lightcoral', 'maroon', 'navy', 'red'])

        # show board
        plt.imshow(self.board, cmap=cmap)
        plt.yticks([])
        plt.xticks([])
        plt.show()


    def convert(self, x, y):
        """
        Converts car coordinates to correct array places.
        """
        #print(x,y)
        col = x - 1
        row = self.size - y
        return [row,col]

    def move_car(self, cars, car, move):
        """
        Moves a car.
        """

        board = self.load_board(cars)

        self.write_output(car[0],move)

        # loop over cars
        for c in cars:

            # if car name matches the car
            if c[0] == car[0]:

                # check if move is valid
                if self.valid_move(board, car, move):

                    # check orientation to decide in which way to move
                    if car[1] == "H":

                        # check direction to move for print statement
                        # if move < 0:
                        #     print(f"Car {car[0]} moved left")
                        # if move > 0:
                        #     print(f"Car {car[0]} moved right")

                        # change car position and update board
                        c[2] = c[2] + move

                        # KARIM:
                        self.board = self.load_board(cars)

                        # # SIRI:
                        # board = self.load_board(cars)
                        return cars, board

                    # repeat for vertical cars
                    if car[1] == "V":
<<<<<<< HEAD
                            # if move > 0:
                            #     print(f"Car {car[0]} moved up")
                            # if move < 0:
                            #     print(f"Car {car[0]} moved down")
=======
                            #if move > 0:
                                #print(f"Car {car[0]} moved up")
                            #if move < 0:
                                #print(f"Car {car[0]} moved down")
>>>>>>> parent of ccb488f... begin of hillclimbing
                            c[3] = c[3] + move
                            return cars, board

        return False

    def valid_move(self, board, car, move):
        """
        Checks if a car move is legal.
        """
        # save row and column coordinates
        row = self.convert(car[2], car[3])[0]
        col = self.convert(car[2], car[3])[1]
        length = car[4]
        orientation = car[1]

        #print("row:", row, "\ncol:", col)

        # check move for horizontal cars
        if orientation == 'H':
            # loop over moves
            for step in range(1,(abs(move)+1)):

                # create 'steps' to check all places between start- and final car position

                # check if car can move left
                if move < 0:

                    # check if car stays on board and position left of car is free
                    if col - step < 0:
                        return False

                    elif board[row][col - step] != '_':
                        # print(f"Car {car[0]} can't go left")
                        return False

                # repeat for right side
                elif move > 0:
                    if col+step+(length-1) >= self.size:
                        return False

                    elif board[row][col+step+(length-1)] != '_':
                        # print(f" Car {car[0]} can't go right")
                        return False

        # repeat for vertical cars

        elif orientation == 'V':
            for step in range(1,(abs(move)+1)):
                if move < 0:
                    if row + step >= self.size:
                        return False

                    elif board[row + step][col] != '_':
                        # print(f"Car {car[0]} can't go down")
                        return False
                elif move > 0:
                    if row - step - (length-1) < 0:
                        return False

                    elif board[row - step - (length-1)][col] != '_' :
                        # print(f"Car {car[0]} can't go up")
                        return False


        return True


    def won(self):
        """
        Checks if the red car can drive through the exit of the board.
        If so, the game is won.
        """

        # retrieve red car row on board
        red_car = self.cars[-1]
        coordinates = self.convert(red_car[2], red_car[3])
        row = coordinates[0]



        for i in reversed(range(self.size)):
                if self.board[row][i] == 'X':
                    return True

                elif self.board[row][i] != '_':
                    return False



    def write_output(self, car, move):
        with open('output.csv',mode='a+', newline='') as output:
            output_writer = csv.writer(output, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            output_writer.writerow([car, move])

    def _repr_(self):
        return self.board
