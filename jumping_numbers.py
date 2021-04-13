def is_jumping_number(number: int) -> bool:
    """Checks if the number is jumping number.

    Parameters
    ----------
    number: int
        The number to check if it is jumping number or not.

    Returns
    -------
    bool
        Whether the number is jumping number or not.

    """
    number_str = str(number)
    for index in range(len(number_str) - 1):
        if abs(int(number_str[index]) - int(number_str[index+1])) != 1:
            return False

    return True


def get_jumping_numbers(limit: int) -> list[int]:
    """Get all the jumping numbers less than or greater to limit.

    Parameters
    ----------
    limit: int
        The limit upto which the find the jumping jumping_numbers.

    Returns
    -------
    list[int]
        A list of all jumping numbers less than or equal to limit.

    """
    jumping_numbers = []
    for i in range(limit):
        if is_jumping_number(i):
            jumping_numbers.append(i)

    return jumping_numbers


if __name__ == "__main__":
    print(get_jumping_numbers(int(input("Enter the limit: "))))
