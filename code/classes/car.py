class Car:
    def __init__(self, name, orientation, x, y, length):

        # returns list of info for each car
        self.info = [name, orientation, x, y, length]
        # print(f" {self.orientation}, {self.coordinates}, {self.length}")

    def move(self):
            pass

    def won(self):
        pass
        # if rode auto staat op plek 3,6 --> win

    def __repr__(self):
        return(f"Car:{self.name}:{self.orientation}, {self.x}, {self.y}, {self.length}")
