# these imports are for plotting the board
import matplotlib as mpl
from matplotlib import pyplot as plt
from matplotlib import colors
import numpy as np

class Board:
    def __init__(self, size, cars):
        self.size=size
        self.cars=cars
        self.board = self.load_board()
        hoi = self.print_board()

    def load_board(self):
        """
        Loads default empty board.
        """
        # VOOR 10-1: willen we list in list maken? Zodat we erover heen kunnen loopen?
        # Maakt een bord van n*n
        board = [['O' for g in range(self.size)] for h in range(self.size)]

        for x in range(self.size):
            for y in range(self.size):
                for car in self.cars:
                    if int(car[2]) == (y+1) and int(car[3]) == (x+1):
                        if car[1]=='H':
                            # if coordinate is good, print coordinates
                            # else, print empty
                            for i in range(int(car[4])):
                                board[(self.size-(x+1))][(y+i)]=car[0]

                        if car[1]=='V':
                            for i in range(int(car[4])):
                                board[(self.size-(x+i+1))][(y)]=car[0]
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

    def _repr_(self):
        return self.board
