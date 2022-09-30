#!/usr/bin/python3
def remove_char_at(str, n):
    return ''.join(i for i in str if str.index(i) != n)
