import random


class Rectangle:
    def __init__(self, length, width, number):
        self.length = length
        self.width = width
        self.number = number

    def calculate_area(self):
        return self.length * self.width


rectangles = ["first", "second", "third", "forth"]


def calculation():
    areas = []
    for i in range(len(rectangles)):
        rectangles[i] = Rectangle(random.randint(1, 100), random.randint(1, 100), i)
    for element in rectangles:
        print(element.length, element.width, sep=" ")
        areas.append(rectangles[i].calculate_area())
    print("Areas of rectangles are : {} ".format(areas))
    max_area = max(areas)
    print("The max area is {}".format(max_area))
    min_area = min(areas)
    print("The max area is {}".format(min_area))


calculation()
