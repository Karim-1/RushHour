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
        print(board)

    def __repr__(self):
        return self.board
