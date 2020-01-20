# these imports are for plotting the board

from car import Car
from matplotlib import pyplot as plt
from matplotlib import colors
import csv
import matplotlib as mpl


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
        self.board = self.load_board()

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

    def load_board(self):
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
                for car in self.cars:

                    # check for cars at the current coordinate
                    if int(car[2]) == (y+1) and int(car[3]) == (x+1):

                        # loop over length of horizontal car
                        if car[1]=='H':
                            for i in range(int(car[4])):

                                # write the car name
                                board[(self.size-(x+1))][(y+i)]=car[0]

                        # repeat for vertical cars
                        if car[1]=='V':
                            for i in range(int(car[4])):
                                board[(self.size-(x+i+1))][(y)]=car[0]
        return board

    def update_board(self):
        """
        Updates the board.
        """
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
        col = x - 1
        row = self.size - y
        return [row,col]

    def move_car(self, car, move):
        """
        Moves a car.
        """

        cars = self.cars

        # loop over cars
        for c in cars:

            # if car name matches the car
            if c[0] == car[0]:

                # check if move is valid
                if self.valid_move(car, move):

                    # check orientation to decide in which way to move
                    if car[1] == "H":

                        # check direction to move for print statement
                        #if move < 0:
                            #print(f"Car {car[0]} moved left")
                        #if move > 0:
                            #print(f"Car {car[0]} moved right")

                        # change car position and update board
                        c[2] = c[2] + move
                        self.update_board()
                        list = []
                        list.append(self.board)
                        list.append(cars)
                        return list

                    # repeat for vertical cars
                    if car[1] == "V":
                            #if move > 0:
                                #print(f"Car {car[0]} moved up")
                            #if move < 0:
                                #print(f"Car {car[0]} moved down")
                            c[3] = c[3] + move
                            self.update_board()
                            list = []
                            list.append(self.board)
                            list.append(cars)
                            return list

        return False


    def valid_move(self, car, move):
        """
        Checks if a car move is legal.
        """

        # save row and column coordinates
        row = self.convert(car[2], car[3])[0]
        col = self.convert(car[2], car[3])[1]
        length = car[4]

        orientation = car[1]

        # check move for horizontal cars
        if orientation == 'H':

            # loop over moves
            for i in range(abs(move)):

                # create 'steps' to check all places between start- and final car position
                steps = move + i

                # check if car stays on the board
                if (col + steps < 0) or (col + steps + length > self.size):
                    return False

                # check if board is free left of the car
                elif steps < 0:
                    if self.board[row][col + steps] != '_':
                        return False

                # check if board is free right of the car
                elif steps > 0:
                    if self.board[row][col + length + steps - 1] != '_':
                        return False

        # repeat for vertical cars
        for i in range(abs(move)):
            if orientation == 'V':
                steps = move + i
                if (row - length + 1 - steps < 0) or (row + length - steps > self.size):
                    # print("out of bounds")
                    return False
                elif steps < 0:
                    if self.board[row - steps][col] != '_':
                        # print("can't go down baby")
                        return False
                elif steps > 0:
                    if self.board[row - length - steps + 1][col] != '_':
                        # print("can't go up")
                        return False

        return True


    def won(self):
        """
        Checks if the red car can drive through the exit of the board.
        If so, the game is won.
        """

        red_car = self.cars[-1]
        coordinates = self.convert(red_car[2], red_car[3])
        position = coordinates[1]
        i = 0
        k = 0

        # create loop that stays on the board matrix
        while k < self.size-1:
            k = position + i + red_car[4]

            # move one spot right each step
            i+=1

            # return false if one of the steps is blocked
            if self.board[2][k] != '_':
                return False

        # return True if right side of the red car is clear
        return True

    def _repr_(self):
        return self.board
