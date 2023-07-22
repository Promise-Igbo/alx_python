# File: 3-last_digit.py

# Importing the required module
import random

# Generating a random signed number and assigning it to the variable number
number = random.randint(-10000, 10000)

# Extracting the last digit of the number
last_digit = abs(number) % 10

# Printing the number and its last digit
print("Last digit of", number, "is", last_digit, end=" ")

# Checking the conditions and printing the corresponding messages
if last_digit > 5:
    print("and is greater than 5")
elif last_digit == 0:
    print("and is 0")
else:
    print("and is less than 6 and not 0")
