# Leslie Bacajol
# 11/06/21
# Problem 1
# This program prints 10 random integers between 25 and 35

import random

print("You have the following random integers between 25 and 35:")

for i in range(10):
    num = random.randrange(25, 35)
    print(num, end=' ')
