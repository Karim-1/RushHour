from copy import deepcopy
import queue
import numpy as np
#queue = [['O', 'A', 'A', 'B', 'B', 'O'], ['O', 'C', 'C', 'E', 'D', 'D'], ['X', 'X', 'G', 'E', 'O', 'I'], ['F', 'F', 'G', 'H', 'H', 'I'], ['K', 'O', 'L', 'O', 'J', 'J'], ['K', 'O', 'L', 'O', 'O', 'O']]
"""
pseudo:
queue aanmaken

while True:
    voor elk autootje:
        moves checken [laat nieuwe cars returnen, anders False]
            (naar links, rechts, 1 tot self.size stapjes)
            (naar boven, onder)
        elke valid move wordt nieuwe child
    als rode autootje er uit kan:
        won()=True
"""
class BFS:
    size = 6
    cars = [['A', 'H', 2, 6, 2], ['B', 'H', 4, 6, 2], ['C', 'H', 2, 5, 2], ['D', 'H', 5, 5, 2], ['E', 'V', 4, 4, 2], ['F', 'H', 1, 3, 2], ['G', 'V', 3, 3, 2], ['H', 'H', 4, 3, 2], ['I', 'V', 6, 3, 2], ['J', 'H', 5, 2, 2], ['K', 'V', 1, 1, 2], ['L', 'V', 3, 1, 2], ['X', 'H', 1, 4, 2]]
    begin_board = [['O', 'A', 'A', 'B', 'B', 'O'], ['O', 'C', 'C', 'E', 'D', 'D'], ['X', 'X', 'G', 'E', 'O', 'I'], ['F', 'F', 'G', 'H', 'H', 'I'], ['K', 'O', 'L', 'O', 'J', 'J'], ['K', 'O', 'L', 'O', 'O', 'O']]

    def bfs(self):
        x = set()
        dict = {}

        queue = queue.Queue()

        # place the begin board in queue
        queue.put(begin_board)

        while not queue.empty():

            # states = board
            state = queue.get()
            print(state)

            for car in cars:
                for step in range(-size, size):
                    #laat move nieuw board returnen, anders false
                    move = move(car, step, size, state)
                    print("CHECK", move)
                    if (move != False) and (move not in x):
                        # keuzes (onthou vorige boards & exclude)
                        child = deepcopy(state)
                        dict[move] = child

                        if Board.won(move):
                            return dict, move
                        x.add(move)
                        queue.put(child)
            # checken voor winnen, adhv child als board

    def bfs_sequence(self):
        pass