#!/usr/bin/python3
import sys
if __name__ == "__main__":
    argument = len(sys.argv)
    if argument == 1:
        print("{:d} {}".format(0, "arguments."))
    elif argument == 2:
        print("{:d} {}".format(1, "argument:"))
        for i in range(1, argument):
            print("{:d}: {}".format(argument - 1, sys.argv[i]))
    else:
        print("{:d} {}".format(argument - 1, "arguments:"))
        for i in range(1, argument):
            print("{:d}: {}".format(i, sys.argv[i]))
