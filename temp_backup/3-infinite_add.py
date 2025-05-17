#!/usr/bin/python3
import sys

total = 0  # start sum at 0

for i in range(1, len(sys.argv)):
    total += int(sys.argv[i])  # convert argument to integer and add

print("{}".format(total))
