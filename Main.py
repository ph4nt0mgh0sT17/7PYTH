print("Test program in 'test-branch' branch")

from Rectangle import Rectangle

'''
print("\nProgram for calculating the rectangle.")
a = float(input("Input rectangle's side A: "))
b = float(input("Input rectangle's side B: "))

rectangle = Rectangle.createRectangle(a,b)

if rectangle is None:
    print("Your sides are wrong!")
    exit(0)

print(f"Rectangle's ({a}, {b}) perimeter is: {rectangle.calculatePerimeter()} cm\u00b2.")
print(f"Rectangle's ({a}, {b}) area is: {rectangle.calculateArea()} cm\u00b2.")
'''

firstNumber = float(input("First number: "))
secondNumber = float(input("Second number: "))
thirdNumber = float(input("Third number: "))

maximumNumber = max(firstNumber,secondNumber,thirdNumber)
minimumNumber = min(firstNumber,secondNumber,thirdNumber)
middleNumber = (firstNumber+secondNumber+thirdNumber) - maximumNumber - minimumNumber

print(f"{minimumNumber}, {middleNumber}, {maximumNumber}")
