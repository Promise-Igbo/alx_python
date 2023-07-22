# File: 5-print_comb2.py

# Using a loop to print numbers from 0 to 99 in two-digit format, separated by ", "
for i in range(100):
    print("{:02d}".format(i), end=", " if i < 99 else "\n")
