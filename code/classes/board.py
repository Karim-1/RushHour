class Board:
    def __init__(self, size, cars):
        #self.board = self.load_board(size)
        self.size=size
        self.cars=cars

    def load_board(self):
        """
        Loads default empty board.
        """
        # VOOR 10-1: willen we list in list maken? Zodat we erover heen kunnen loopen?
        # Maakt een bord van n*n
        self.Board = [['O' for g in range(self.size)] for h in range(self.size)]
        print(self.cars)
        for x in range(self.size):
            for y in range(self.size):
                for car in self.cars:
                    if int(car[2]) == (y+1) and int(car[3]) == (x+1):
                        if car[1]=='H':
                            # if coordinate is good, print coordinates
                            # else, print empty
                            for i in range(int(car[4])):
                                self.Board[(self.size-(x+1))][(y+1+i-1)]=car[0]

                        if car[1]=='V':
                            for i in range(int(car[4])):
                                self.Board[(self.size-(x+i+1))][(y+1-1)]=car[0]
            print(self.Board)


    def __repr__(self):
        return self.Board
