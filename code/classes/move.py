from board import Board

class Move:
    def __init__(self, car, move, size, loaded_board):
        # retrieve board size from filename
        self.car = car
        self.move = move
        self.size = size
        self.loaded_board = loaded_board
        print("HIJ KOMT HIER")

    def coord_array(self, x, y):
        """
        Convert coordinates to correct array places.
        """
        x = x - 1
        y = self.size - y
        return [y,x]

    def move_car(self):
        """
        Moves a car.
        """
        car = self.car
        cars = Board.cars()
        print(self.car)
        print(cars)
        for c in cars:
            if cars[0] == car[0]:
                # check orientation to decide in which way to move
                if car[1] == "H":
                    # check direction to move
                    if self.valid_move():
                        if self.move < 0:
                            print(f"Car {self.car[0]} moved left")
                        if self.move > 0:
                            print(f"Car {self.car[0]} moved right")
                        c[2] = c[2] + self.move
                        return True

                if self.car[1] == "V":

                    # check direction to move
                    if self.valid_move():
                        if self.move < 0:
                            print(f"Car {self.car[0]} moved down")
                        if self.move > 0:
                            print(f"Car {self.car[0]} moved up")
                        self.car[3] = self.car[3] + self.move
                        return True
                print(self.car)
        return False

    def valid_move(self, board, car, move):
        """
        Checks if a car move is legal.
        """
        # save row and column coordinates
        row = self.convert(car[2], car[3])[0]
        col = self.convert(car[2], car[3])[1]
        length = car[4]
        orientation = car[1]

        #print("row:", row, "\ncol:", col)

        # check move for horizontal cars
        if orientation == 'H':
            # loop over moves
            for step in range(1,(abs(move)+1)):

                # create 'steps' to check all places between start- and final car position

                # check if car can move left
                if move < 0:

                    # check if car stays on board and position left of car is free
                    if col - step < 0:
                        return False

                    elif board[row][col - step] != '_':
                        # print(f"Car {car[0]} can't go left")
                        return False

                # repeat for right side
                elif move > 0:
                    if col+step+(length-1) >= self.size:
                        return False

                    elif board[row][col+step+(length-1)] != '_':
                        # print(f" Car {car[0]} can't go right")
                        return False

        # repeat for vertical cars

        elif orientation == 'V':
            for step in range(1,(abs(move)+1)):
                if move < 0:
                    print("VAL", row, step, self.size)
                    if row + step >= self.size:
                        return False

                    elif board[row + step][col] != '_':
                        # print(f"Car {car[0]} can't go down")
                        return False
                elif move > 0:
                    if row - step - (length-1) < 0:
                        return False

                    elif board[row - step - (length-1)][col] != '_' :
                        # print(f"Car {car[0]} can't go up")
                        return False

        print("VALID MOVE")
        return True
