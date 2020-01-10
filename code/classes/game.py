import csv
from car import Car
from board import Board


# Mentorgesprek notes: class car (x,y, orientatie, length, name)
# class board
# `classs game (car_list, board)
# functie Move_car(iD, direction), als deze wordt aangeroepen, zorg dan dat je game veranderds
# functie Is_win
# functie Is_emptyss
# Mathplotlib gebruiken om vierkantjes te maken om bord te visualiseren `9makkelijker dan je denkt`
# de algorithmes pakken move_cvar


class Game:
    def __init__(self, gameboard_file):
        #self.cars = self.load_cars(gameboard_file)
        #self.size nog dynamisch maken o.b.v. gameboard_file naam
        #self.size = 6
        self.gameboard_file = gameboard_file


    def load_cars(self):
        """
        Loads all cars into the game
        """
        # read through csv gameboard file
        with open(self.gameboard_file, "r") as in_file:
            reader = csv.DictReader(in_file, skipinitialspace=True)
            cars = []

            # create car for each row
            for row in reader:
                coordinates = row['x,y'].split(",")
                car = Car(row['car'], row['orientation'], coordinates[0], coordinates[1], row['length'])
                cars.append(car.info)
            return cars


    # in string method functie maken die bord simuleert
    def __repr__(self):
        s=""
        for c in self.cars:
            s+=str(c)
        return s
        #return(f"Auto's:{self.cars}")

    def move_car(self, car_name, orientation, direction):
        if orientation == "H":
            print(self.cars)
            print("Move")
            pass
        elif orientation =="V":
            pass

# NOTE: Dit weghalen bij het inleveren, aparte "main.py" file maken
if __name__ == "__main__":
    lvl1 = Game('../../gameboards/Rushhour6x6_1.csv')
#    print(lvl1.cars[0][0])
#    car_name = lvl1.cars[0][0]
#    orientation = lvl1.cars[0][1]
#    print(orientation)
#    direction = -1
#    print(direction)
#    lvl1.move_car(car_name, orientation, direction)
    cars = lvl1.load_cars()
    current_board = Board(6, cars)
    current_board.load_board()
