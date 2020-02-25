"""
print("Test program in 'test-branch' branch")

from Rectangle import Rectangle

print("\nProgram for calculating the rectangle.")
a = float(input("Input rectangle's side A: "))
b = float(input("Input rectangle's side B: "))

rectangle = Rectangle.createRectangle(a, b)

if rectangle is None:
    print("Your sides are wrong!")
    exit(0)

print(f"Rectangle's ({a}, {b}) perimeter is: {rectangle.calculatePerimeter()} cm\u00b2.")
print(f"Rectangle's ({a}, {b}) area is: {rectangle.calculateArea()} cm\u00b2.")

"""

""" Gets the maximum number """
def max_number(number1, number2, number3):
    maximum = number1

    if maximum < number2:
        maximum = number2

    if maximum < number3:
        maximum = number3

    return maximum

""" Gets the minimum number """
def min_number(number1, number2, number3):
    minimum = number1

    if minimum > number2:
        minimum = number2

    if minimum > number3:
        minimum = number3

    return minimum


first_number = float(input("First number: "))
second_number = float(input("Second number: "))
third_number = float(input("Third number: "))

maximum_number = max_number(first_number, second_number, third_number)
minimum_number = min_number(first_number, second_number, third_number)
middle_number = (first_number + second_number + third_number) - maximum_number - minimum_number
print(f"{minimum_number}, {middle_number}, {maximum_number}")
