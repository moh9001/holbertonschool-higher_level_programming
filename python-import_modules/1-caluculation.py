#!/usr/bin/python3
from calculator_1 import add, sub, mul, div  # only one use of calculator_1

a = 10  # defined in one line
b = 5   # defined in another line

print("{} + {} = {}".format(a, b, add(a, b)))
print("{} - {} = {}".format(a, b, sub(a, b)))
print("{} * {} = {}".format(a, b, mul(a, b)))
print("{} / {} = {}".format(a, b, div(a, b)))
