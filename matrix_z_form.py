from typing import Iterable


def get_matrix() -> Iterable[Iterable[int]]:
    """Get the square integer matrix from the user.

    Returns
    =======
    Iterable[Iterable[int]]
        The square integer matrix input from the user.

    """
    length = int(input("Enter the length of the square matrix: ").split()[0])
    matrix = []
    print("Input the matrix: ")
    for _ in range(length):
        matrix.append(tuple(map(int, input().split()[:length])))

    return matrix


def print_z_matrix(matrix: Iterable[Iterable[int]]) -> None:
    """Print the z form of the matrix.

    Arguments
    =========
    matrix: Iterable[Iterable[int]]
        The square matrix to print the Z form.

    """
    print("Note: if the matrix inputted isn't square, " +
          "all the values outside the square will be ignored")

    print(" ".join([str(value) for value in matrix[0]]), end=" ")

    slant_position = len(matrix[0]) - 2

    for i in range(1, len(matrix) - 1):
        print(matrix[i][slant_position], end=" ")
        slant_position -= 1

    print(" ".join([str(value) for value in matrix[-1]]))


if __name__ == "__main__":
    matrix = get_matrix()
    print_z_matrix(matrix)
