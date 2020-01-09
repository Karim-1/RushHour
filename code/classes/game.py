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
        self.cars = self.load_cars(gameboard_file)

    def load_cars(self, gameboard_file):
        """
        Loads all cars into the game
        """
        # read through csv gameboard file
        with open(gameboard_file, "r") as in_file:
            reader = csv.DictReader(in_file, skipinitialspace=True)
            cars = []

            # create car for each row
            for row in reader:
                car = Car(row['car'], row['orientation'], row['x,y'], row['length'])
                cars.append(car)

            return cars

    # in string method functie maken die bord simuleert
    def __repr__(self):
        s=""
        for c in self.cars:
            s+=str(c)
        return s
        #return(f"Auto's:{self.cars}")


# NOTE: Dit weghalen bij het inleveren, aparte "main.py" file maken
if __name__ == "__main__":
    # Game('gameboards/Rushhour6x6_1.csv')
    pass
