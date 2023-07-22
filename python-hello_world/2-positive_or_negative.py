# File: 2-positive_or_negative.py

# Importing the required module
from random import randint

# Generating a random signed number and assigning it to the variable number
number = randint(-10, 10)

# Printing the number and its sign
if number > 0:
    print(number, "is positive")
elif number == 0:
    print(number, "is zero")
else:
    print(number, "is negative")
