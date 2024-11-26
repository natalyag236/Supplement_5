import math
def square_root(number):
    """Calculate the sqaure root of a given number.

    Args:
        number (float): the number to calculate the sqaure root. Must be non-negative.

    Raises:
        ValueError: If the input number is negative

    Returns:
        float: the sqaure root of the input number
    """
    if number < 0:
        raise ValueError("Cannot calculate the square root of a negative number")
    return math.sqrt(number)

def test_square_root_():
    assert square_root(9) == 3