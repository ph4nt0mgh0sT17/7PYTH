class Rectangle:

    def __init__(self, sideA, sideB):
        self.sideA = sideA
        self.sideB = sideB

    @staticmethod
    def createRectangle(sideA, sideB):
        if sideA == sideB or sideA <= 0 or sideB <= 0:
            return None

        return Rectangle(sideA, sideB)

    def calculatePerimeter(self):
        return 2 * (self.sideA + self.sideB)

    def calculateArea(self):
        return self.sideA * self.sideB
