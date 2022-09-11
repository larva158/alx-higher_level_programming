#!/usr/bin/python3
for i in range(10):
    for k in range(10):
        if i < k:
            if (i * 10 + k) != 89:
                print("{}{},".format(i, k), end=' ')
            else:
                print("{}{}".format(i, k))
