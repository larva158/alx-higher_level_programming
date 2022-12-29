#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argument = len(sys.argv)
    num = 0
    if argument == 1:
        print("{:d}".format(0))
    else:
        for i in range(1, argument):
            num += int(sys.argv[i])
        print(num)

