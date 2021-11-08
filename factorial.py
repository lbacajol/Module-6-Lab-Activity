# Leslie Bacajol
# 11/06/21
# Problem 6
# This program calculates the factorial of a user input value

import math

value = int(input("Enter a number for computing its factorial:"))

for i in range(1):
    ans = math.factorial(value)
    print("The value from the factorial function is", ans)
