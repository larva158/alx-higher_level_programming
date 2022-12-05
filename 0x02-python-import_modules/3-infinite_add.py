#!/usr/bin/python3
import sys
if __name__ == "__main__":
    sum = 0
    if len(sys.argv) == 1:
        print("{:d}".format(0))
    else:
        for num in sys.argv:
            sum += int(num)
        print("{:d} + {:d}".format(sum, num))
