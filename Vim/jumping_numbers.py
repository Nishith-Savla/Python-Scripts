def is_jumping_number(number):
    """Checks if the number is jumping number

    :number: TODO
    :returns: TODO

    """
    number_str = str(number)
    for index in range(len(number_str) - 1):
        if abs(int(number_str[index]) - int(number_str[index+1])) != 1:
            return False

    return True
    

def get_jumping_numbers(limit):
    """Get all the jumping numbers less than or greater to limit

    :limit: TODO
    :returns: TODO

    """
    jumping_numbers = []
    for i in range(limit):
        if is_jumping_number(i):
            jumping_numbers.append(i)

    return jumping_numbers


if __name__ == "__main__":
    print(get_jumping_numbers(int(input("Enter the limit: "))))
