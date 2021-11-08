# Leslie Bacajol
# 11/06/21
# Problem 4
# This program computes the approximation of pi and then prints that value
# Two different methods
# one from the math.pi from the math module

from math import acos  # first math function call

import math  # second math function call

print("This is an approximate for pi:")  # explanation sentence
# first math function for pi
pi = round(2 * acos(0.0), 3)
print(pi)


print("This is another approximation for pi:")  # second explanation sentence
# second math function for pi
print(math.pi)
