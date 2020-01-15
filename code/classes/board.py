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

    def update_board(self):
        self.board = self.load_board()

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
                if self.board[i][j] == 'O':
                    self.board[i][j]=0
                # if car is red, set 1
                elif self.board[i][j] == 'X':
                    self.board[i][j] = 1
                # else, set to value as calculated above
                else:
                    self.board[i][j] = dict[self.board[i][j]]

        # list of possible colors, ranging from grey to red
        cmap = colors.ListedColormap(['grey','yellow', 'orange', 'green', 'purple', 'lightcoral', 'lightcyan', 'aquamarine', 'mediumspringgreen', 'fuchsia', 'mediumslateblue', 'darkviolet', 'dodgerblue', 'pink', 'goldenrod', 'navajowhite', 'peachpuff', 'olivedrab', 'teal', 'palevioletred', 'papayawhip', 'maroon', 'navy', 'red'])

        # show board
        plt.imshow(self.board, cmap=cmap)
        plt.yticks([])
        plt.xticks([])
        plt.show()


    def coord_array(self, x, y):
        """
        Convert coordinates to correct array places.
        """
        x = x - 1
        y = self.size - y
        return [y,x]

    def move_car(self, car, move):
        """
        Moves a car.
        """

        cars = self.cars
        for c in cars:
            if c[0] == car[0]:
                # check orientation to decide in which way to move
                if car[1] == "H":

                    # check if move is valid
                    if self.valid_move(car, move):
                        # check direction to move
                        if move < 0:
                            print(f"Car {car[0]} moved left")
                        if move > 0:
                            print(f"Car {car[0]} moved right")
                        c[2] = c[2] + move

                if car[1] == "V":
                    if self.valid_move(car, move):
                        if move < 0:
                            print(f"Car {car[0]} moved down")
                        if move > 0:
                            print(f"Car {car[0]} moved up")
                        c[3] = c[3] + move
        self.update_board()


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
                    if self.board[row + steps][col] != 'O':
                        # print("Can't move down")
                        return False
                elif steps > 0:
                    if self.board[row - steps][col] != 'O':
                        # print("Can't move up")
                        return False

        # print("Valid move")
        return True


    def won(self):
        """
        Checks if the red car can drive through the exit of the parking lot.
        If so, the game is won.
        """

        if self.cars[-1][3] == self.size - 1:
            return True
        return False

    def _repr_(self):
        return self.board
