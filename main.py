import math
def square_root(number):
    if number < 0:
        raise ValueError("Cannot calculate the square root of a negative number")
    return math.sqrt(number)

def test_square_root_():
    assert square_root(9) == 3