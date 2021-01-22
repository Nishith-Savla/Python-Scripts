import math

size = int(input())
spaces = 0 if size % 2 == 0 else -1
for row in range(size):
    if spaces > 0:
        star_count = (size - spaces)//2
        print("*"*star_count, end="")
        print(" "*spaces, end="")
        print("*"*star_count)
    else:
        print("*"*size)

    if row < math.floor(size/2) - 1:
        spaces += 2
    else:
        spaces -= 2
