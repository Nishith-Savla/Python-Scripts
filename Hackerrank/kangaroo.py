import math
import os
import random
import re
import sys


def kangaroo(x1, v1, x2, v2):
    if (x1 >= x2 and v1 >= v2) or (x1 <= x2 and v1 <= v2):
        return "NO"
    d1 = x1
    d2 = x2
    while d1 != d2:
        if (v1 >= v2 and d1 >= d2) or (v1 <= v2 and d1 <= d2):
            return "NO"
        d1 += v1
        d2 += v2
    return "YES"


if __name__ == '__main__':
    x1V1X2V2 = input().split()

    x1 = int(x1V1X2V2[0])

    v1 = int(x1V1X2V2[1])

    x2 = int(x1V1X2V2[2])

    v2 = int(x1V1X2V2[3])

    print(kangaroo(x1, v1, x2, v2))
