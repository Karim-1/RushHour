class Board:
    def __init__(self, size):
        self.board = self.load_board(size)

    def load_board(self, size):
        """
        Loads default empty board.
        """
        # VOOR 10-1: willen we list in list maken? Zodat we erover heen kunnen loopen?
        # xx
        for i in range(size):
            for j in range(size):
                pass

    def __repr__(self):
        return(self.board)
