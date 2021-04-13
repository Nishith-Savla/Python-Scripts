"""https://www.hackerrank.com/challenges/find-angle/problem"""

import math


def calculate_angle(x, y):
    return round(math.degrees(math.atan(x/y)))


if __name__ == '__main__':
    print(calculate_angle(10, 10), chr(176), sep='')
