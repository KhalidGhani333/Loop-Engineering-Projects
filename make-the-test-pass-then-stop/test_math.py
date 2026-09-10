from math_utils import add, is_even, largest


def test_add_returns_the_sum():
    assert add(2, 3) == 5


def test_is_even_detects_even_numbers():
    assert is_even(4) is True
    assert is_even(7) is False


def test_largest_returns_the_biggest_number():
    assert largest([3, 9, 2]) == 9
