from typing import Iterable


def get_combination_indices(length: float) -> list[tuple[float]]:
    """Get the combination indices till the length specified.

    Parameters
    ----------
    length: int
        The length of the array.

    Returns
    -------
    list[tuple[float]]
        The list of tuple of indices of combination.

    """
    combination_indices = []
    for i in range(length):
        for j in range(i+1, length):
            if (j, i) not in combination_indices:
                combination_indices.append((i, j))

    return combination_indices


def get_combinations(values: Iterable[float]) -> list[tuple[float]]:
    """Get all unique combinations of the values iterable.

    Parameters
    ----------
    values: Iterable[float]
        The iterable to get the combinations from.

    Returns
    -------
    list[tuple[float]]
        The list containing all combinations of the given iterable.

    """
    return [
        (values[i], values[j]) for i, j in get_combination_indices(len(values))
    ]


def get_sum_of_products_from_iterable(
        combinations: Iterable[Iterable[float]]) -> float:
    """Get the sum of products of each combination from the iterable.

    Parameters
    ----------
    combinations: Iterable[Iterable[float]]
        Iterable of all combinations.

    Returns
    -------
    float
        Sum of products of all combinations.

    """
    return sum([i*j for i, j in combinations])


def get_sum_of_products(values: list[float]) -> float:
    """Get the sum of products for each combination of numbers in value list.

    Parameters
    ----------
    values: list[float]
        The list of numbers.

    Returns
    -------
    float
        Sum of products of all combinations.

    """
    return sum([i*j for i, j in get_combinations(values)])


if __name__ == "__main__":
    values = tuple(map(float, input('Enter the numbers: ').split()))
    print(get_sum_of_products(values))
