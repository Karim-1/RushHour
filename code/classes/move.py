class Move:
    def __init__(self, car, move, size, loaded_board):
        # retrieve board size from filename
        self.car = car
        self.move = move
        self.size = size
        self.loaded_board = loaded_board

    def coord_array(self, x, y):
        """
        Convert coordinates to correct array places.
        """
        x = x - 1
        y = self.size - y
        return [y,x]

    def move_car(self):
        """
        Moves the car
        """

        # check orientation to decide in which way to move
        if car[1] == "H":
            # check direction to move
            if self.valid_move():
                if self.move < 0:
                    print(f"Car {self.car[0]} moved left")
                if self.move > 0:
                    print(f"Car {self.car[0]} moved right")
                self.car[2] = self.car[2] + self.move
            else:
                return False

        if self.car[1] == "V":

            # check direction to move
            if self.valid_move():
                if self.move < 0:
                    print(f"Car {self.car[0]} moved down")
                if self.move > 0:
                    print(f"Car {self.car[0]} moved up")
                self.car[3] = self.car[3] + self.move
            else:
                return False
        print(self.car)

    def valid_move(self):
        """
        Checks if the move is a valid move
        """
        # save x and y coordinates
        row = self.coord_array(self.car[2], self.car[3])[0]
        col = self.coord_array(self.car[2], self.car[3])[1]
        orientation = self.car[1]

        # check move for horizontal cars
        if orientation == 'H':
            for i in range(abs(self.move)):
                steps = self.move + i

                # check if car stays on the board
                if (col + steps < 0) or (col + steps + self.car[4] > self.size):
                    return False
                elif steps < 0:
                    if self.loaded_board[row][col + steps] != 'O':
                        return False
                elif steps > 0:
                    if self.loaded_board[row][col + self.car[4] + steps - 1] != 'O':
                        return False

        # check move for vertical cars
        for i in range(abs(self.move)):
            if orientation == 'V':
                steps = self.move + i
                if ((row - steps) < 0) or (row-steps+self.car[4] > self.size):
                    return False
                elif steps < 0:
                    if self.loaded_board[row - steps][col] != 'O':
                        return False
                elif steps > 0:
                    if self.loaded_board[row - self.car[4] - steps + 1][col] != 'O':
                        return False

        print("Valid move")
        return True
