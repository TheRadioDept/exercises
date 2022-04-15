import random


class Rectangle:
    """
    create class Rectangle with parameters length and width.
    """
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        """
        Function to calculate area of Rectangle
        """
        return self.length * self.width


rectangles = ["first", "second", "third", "forth"]


def calculation():
    """
    Function to create four objects of class Rectangle and apply `calculate_area()` function to calculate their areas.
    Then store these calculated areas and find maximum and minimum value out of them.
    """
    areas = []
    for i in range(len(rectangles)):
        rectangles[i] = Rectangle(random.randint(1, 100), random.randint(1, 100))
        areas.append(rectangles[i].calculate_area())
    for element in rectangles:
        print(element.length, element.width, sep=" ")
    print("Areas of rectangles are : {} ".format(areas))
    max_area = max(areas)
    print("The max area is {}".format(max_area))
    min_area = min(areas)
    print("The max area is {}".format(min_area))


calculation()
