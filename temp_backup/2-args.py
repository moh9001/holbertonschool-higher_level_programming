#!/usr/bin/python3
import sys

argc = len(sys.argv) - 1  # number of actual arguments (excluding program name)

if argc == 0:
    print("0 arguments.")
elif argc == 1:
    print("1 argument:")
else:
    print("{} arguments:".format(argc))

for i in range(1, len(sys.argv)):
    print("{}: {}".format(i, sys.argv[i]))
