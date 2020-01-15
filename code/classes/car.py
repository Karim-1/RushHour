class Car:
    def __init__(self, name, orientation, x, y, length):
        # returns list of info for each car
        self.info = [name, orientation, x, y, length]

    def __repr__(self):
        return(f"Car:{self.name}:{self.orientation}, {self.x}, {self.y}, {self.length}")
