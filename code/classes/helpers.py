def won(self):
    """
    returns True when car "x" reaches the right side of the board
    """
    # if red car reaches the right side of the board, game is won
    if self.cars[-1][3] == self.size - 1:
        return True
    return False
