# My failed try to solve the rainwater problem

from typing import List, Iterator


def check_is_lower(island_mat: List[List[int]], rows: int, cols: int, i: int, j: int) -> bool:
    """Checks if the current area is lower than the surroundings.

    Parameters
    ----------
    island_mat: List[List[int]]
        The matrix composed of the cells containing the height of the region.
    rows: int
        The number of rows of the matrix.
    cols: int
        The number of colums of the matrix.
    i: int
        The index of the current row.
    j: int
        The index of the current column in the row.

    Returns
    -------
    is_lower: bool
        True if the surrounding have more heights(there are height on all four sides greater than the current height),
         else False
    """
    sides_greater = 0
    current_elem = island_mat[i][j]

    # Checking upwards
    for b in range(j, -1, -1):
        if island_mat[i][b] > current_elem:
            sides_greater += 1
            break

    # Checking downwards
    for b in range(j, cols):
        if island_mat[i][b] > current_elem:
            sides_greater += 1
            break

    # Checking on the left
    for a in range(i, -1, -1):
        if island_mat[a][j] > current_elem:
            sides_greater += 1
            break

    # Checking on the right
    for a in range(i, rows):
        if island_mat[a][j] > current_elem:
            sides_greater += 1
            break

    return sides_greater == 4


def calculate_water_collected(island_mat: List[Iterator[int]], rows: int, cols: int) -> int:
    """Calculates the total number of cells (regions) where water will be collected after rain.

    Parameters
    ----------
    island_mat: List[List[int]]
        The matrix composed of the cells containing the height of the region.
    rows: int
        The number of rows of the matrix.
    cols: int
        The number of colums of the matrix.

    Returns
    -------
    total_water_collected: int
        The number of cells where water will be collected after rain.
    """
    total_water_collected = 0
    for i in range(1, rows - 1):
        for j in range(1, cols - 1):
            if check_is_lower(island_mat, rows, cols, i, j):
                total_water_collected += 1
    return total_water_collected


if __name__ == '__main__':
    print(calculate_water_collected(
        [[3, 5, 5], [5, 4, 5], [5, 5, 5]], 3, 3))
    print(calculate_water_collected(
        [[5, 5, 5, 1], [5, 1, 1, 5], [5, 1, 5, 5], [5, 1, 5, 8]], 4, 4))
    print(calculate_water_collected(
        [[2, 2, 2], [2, 1, 2], [2, 1, 2], [2, 1, 2]], 4, 3))

    for case in range(int(input("Enter the number of test cases: "))):
        rows, cols = map(int, input(
            "Enter the numbers of rows and columns: ").split())
        matrix: list[Iterator[int]] = []
        print("Enter the entries rowwise:")
        for i in range(rows):  # A for loop for row entries
            matrix.append(map(int, input().split()))
        calculate_water_collected(matrix, rows, cols)
