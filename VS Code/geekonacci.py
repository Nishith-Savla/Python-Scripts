import sys


def get_geekonacci_number(a, b, c, N):
    arr = [a, b, c]
    while len(arr) < N:
        length = len(arr)
        arr.append(arr[length-1] + arr[length-2] + arr[length-3])
    return arr[length]


if __name__ == "__main__":
    print(get_geekonacci_number(*list(map(int, sys.argv[1:]))))
