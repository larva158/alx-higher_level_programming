#!/usr/bin/python3
def print_last_digit(number):
    number = number % 10
    if number < 0:
        number = (number % 10) * (-1)
    return number


print(print_last_digit(98), end='')
print(print_last_digit(0), end='')
r = print_last_digit(-1024)
print(r)
