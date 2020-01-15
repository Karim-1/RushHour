# these imports are for plotting the board
import matplotlib as mpl
from matplotlib import pyplot as plt
from matplotlib import colors
import csv
from car import Car


class Board:
    """
    This class ensures that the board is represented in a gameboard-like style.
    """

    def __init__(self, size, gameboard_file):
        """
        Intialize board parameters
        """

        self.size = size
        self.gameboard_file = gameboard_file
        self.cars = self.load_cars()
        self.board = self.load_board()

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
        Loads default empty board
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

    def print_board(self):
        """
        Prints the board in a gameboard-structure
        """

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
                if self.board[i][j] == 'O':
                    self.board[i][j]=0

                # if car is red, set 1
                elif self.board[i][j] == 'X':
                        self.board[i][j] = 1

                # else, set to value as calculated above
                else:
                    self.board[i][j] = dict[self.board[i][j]]

        # list of possible colors, ranging from grey to red
        cmap = colors.ListedColormap(['lightgrey','yellow', 'orange', 'green', 'purple', 'lightcoral', 'lightcyan', 'aquamarine', 'mediumspringgreen', 'fuchsia', 'mediumslateblue', 'darkviolet', 'dodgerblue', 'pink', 'goldenrod', 'navajowhite', 'peachpuff', 'olivedrab', 'teal', 'palevioletred', 'papayawhip', 'maroon', 'navy', 'red'])

        # show board
        plt.imshow(self.board, cmap=cmap)
        plt.yticks([])
        plt.xticks([])
        plt.show()

    def _repr_(self):
        return self.board
