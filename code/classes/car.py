class Car:
    def __init__(self, name, orientation, coordinates, length):
        self.name = name
        self.orientation = orientation
        self.coordinates = coordinates
        self.length = length
        # print(f" {self.orientation}, {self.coordinates}, {self.length}")
        print(f"Car {self.name}:{self.orientation}, {self.coordinates}, {self.length}")

    def move(self):
            pass

    def won(self):
        pass
        # if rode auto staat op plek 3,6 --> win

    def __repr__(self):
        return(f"{self.orientation}, {self.coordinates}, {self.length}")
