"""
This module provides a function to find the opposite
number given a range and a starting number.
"""


def find_opposite_number(n, first_num):
    """Find the opposite number in a given range."""

    if not isinstance(n, int) or n <= 0 or n % 2 != 0:
        return False

    if not isinstance(first_num, int) or first_num < 0 or first_num >= n:
        return False

    return (first_num + n // 2) % n


assert find_opposite_number(10, 2) == 7, \
    "Fail: Expected opposite of 2 in range 10 to be 7"

assert find_opposite_number(12, 10) == 4, \
    "Fail: Expected opposite of 2 in range 10 to be 7"

assert not find_opposite_number(7, 2), "Expected False for odd range 7"
