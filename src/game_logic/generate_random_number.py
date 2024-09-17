from random import randint


def random_number_generator(start: int = 1, end: int = 100) -> int:
    """generate a random number by default between 1 to 100

    Args:
        start (int, optional): Defaults to 1.
        end (int, optional): Defaults to 100.

    Returns:
        int: _description_
    """
    return randint(start, end)


if __name__ == "__main__":
    print(random_number_generator())
