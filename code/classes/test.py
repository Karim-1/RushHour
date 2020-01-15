# these imports are for plotting the board
import matplotlib as mpl
from matplotlib import pyplot as plt
from matplotlib import colors
import numpy as np

class Board:
    def __init__(self, size, cars):
        #self.board = self.load_board(size)
        self.size=size
        self.cars=cars
        self.board = self.load_board()

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

        print("Board: ")
        print(board[1])
        m = np.zeros((self.size,self.size))
        #m = np.zeros((1,20))

        # Maak dictionary van vorm {A: getal}
        dict = {}
        for i in range(len(self.cars)):
                    # genereer voor elke auto een getal tussen 0 en 1
                j=i+1
                dict[self.cars[i][0]] = (1/len(self.cars))*j
        print(dict)



        for row in board:
            for col in row:
                if col == 'O':
                    m[row][col]=0
                elif col == 'X':
                    m[row][col]=1
                else:
                    pass




        #print("M", m)
        for i in range(self.size):
            # if plek is leeg: m[x,y]=0
            # if plek is rood....
            m[1,i] = ((i)*5)/100.0
        print(m)
        cmap = colors.ListedColormap(['grey','yellow','red', 'orange', 'green', 'purple'])
        #m = m.reshape((self.size, self.size))
        plt.imshow(m, cmap=cmap)
        plt.yticks([])
        plt.xticks([])
        plt.show()

        #make a color map of fixed colors (not working yet)
        #cmap = colors.ListedColormap(['blue','yellow','red', 'orange'])
        #bounds = [0,10,20]
        #print(bounds)
        #norm = colors.BoundaryNorm(bounds, cmap.N)
        #print(norm)

                    # self.size=2
                    # # Specify amount of rows and colors in the image
                    # image=np.zeros(self.size*self.size)
                    #
                    # # Set every other cell to a random number (this would be your data)
                    # #image[::] = np.random.random(self.size*self.size)
                    # #print(image)
                    # image[::] = [1, 2, 3, 4]
                    # # Reshape things into a size*size grid.
                    # image = image.reshape((self.size, self.size))
                    #
                    # pyplot.xticks([])
                    # pyplot.yticks([])
                    # pyplot.matshow(image)
                    # pyplot.show()

        # tell imshow about color map so that only set colors are used
        #img = pyplot.imshow(zvals,interpolation='nearest',
        #                    cmap = cmap)

        # board = []
        # d = 6
        # for i in range(d):
        #     row = []
        #     for j in range(d):
        #         row.append(d*d-1-i-d*j)
        #     board.append(row)
        # board[blankx][blanky] = d * d
        # print(board)

        return board

    def _repr_(self):
        return self.board

    def setup(self):
        size(800,600)

    # def draw(self):
    #     w = 70
    #     x,y =0,0
    #     for row in board:
    #         for col in row:
    #             rect(x, y, w, w)
    #             x = x + w
