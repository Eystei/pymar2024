"""
This module provides a function to find the opposite
number given a range and a starting number.
"""


def find_opposite_number(n, first_num):
    """Find the opposite number in a given range."""

    if not isinstance(n, int) or n <= 0 or n % 2 != 0:
        return "n must be a positive, even integer."

    if not isinstance(first_num, int) or first_num < 0 or first_num >= n:
        return "first_number must be an integer between 0 and n-1."

    return (first_num + n // 2) % n


if __name__ == '__main__':
    print(find_opposite_number(10, 2))
    print(find_opposite_number(9, 2))
    print(find_opposite_number(10, 10))
