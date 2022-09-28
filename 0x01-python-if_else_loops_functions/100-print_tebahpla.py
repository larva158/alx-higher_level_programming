#!/usr/bin/python3
for i in reversed(range(97, 123)):
    if i % 2:
        print("{:c}".format(i).upper(), end="")
    else:
        print("{:c}".format(i), end="")
