#!/usr/bin/python3
def print_last_digit(number):
    num = 0
    if number < 0:
        num = number * (-1)
        lst_number = (num % 10) * (1)
    else:
        lst_number = number % 10
    print(f"{lst_number}", end="")
    return lst_number


print_last_digit(98)
print_last_digit(0)
r = print_last_digit(-1024)
print(r)
