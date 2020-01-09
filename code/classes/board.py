class Board:
    def __init__(self, size):
        self.board = self.load_board(size)

    def load_board(self, size):
        """
        Loads default empty board.
        """
        # VOOR 10-1: willen we list in list maken? Zodat we erover heen kunnen loopen?
        # xx
        Matrix = [[0 for x in range(size)] for y in range(size)]
        print(Matrix)
        for i in range(size):
            for j in range(size):
                print("# ", end='')
            print("\n")

    def __repr__(self):
        return self.board
