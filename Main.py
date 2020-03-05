# Initializing of variables for counting the numbers
result = 0
counter = 0

# Gets number from the input
while True:
    current_number = int(input("Type a number: "))

    # If the number is 0 don't count it and break the while
    if current_number == 0:
        break;

    result += current_number
    counter += 1


sum = result

# The average is calculated only if the counter is bigger than zero -> Division by zero is forbidden
if counter > 0:
    average = result / counter

print(sum)
print(round(average, 2))
