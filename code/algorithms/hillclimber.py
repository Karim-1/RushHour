from .randomize import randomize
import numpy


def hillclimber(cars):
    print("inside hillclimber algorithms")
    random_solution = randomize(cars)
    # steps_amount = randomize(cars)
    steps = random_solution[0]
    steps_count = random_solution[1]
    print("steps:",steps_count)
    firsthalf = round(steps_count/2)
    print("firsthalf", firsthalf)
    print(steps[firsthalf][1])


class Hillclimber():

    def __init__(self, cars):
        self.cars = cars


    def run(self):
        random_solution = randomize(self.cars)
        steps = random_solution[0]
        steps_count = random_solution[1]
        firsthalf = round(steps_count/2)

        print("steps:",steps_count)
        #
        # print("firsthalf", firsthalf)
        # print(steps[firsthalf][1])
        # print(steps[steps_count][1])

    def won():
        pass
        # print("inside hillclimber algorithms")
        # random_solution = randomize(cars)
        # # steps_amount = randomize(cars)
        # steps = random_solution[0]
        # steps_count = random_solution[1]
        # print("steps:",steps_count)
        # firsthalf = round(steps_count/2)
        # print("firsthalf", firsthalf)
        # print(steps[firsthalf][1])
        # print(steps[steps_count][1])
