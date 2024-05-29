"""
Module for counting consecutive characters.
"""

from itertools import groupby

A = "cccbba"  # == "c3b2a"
B = "abeehhhhhccced"  # == "abe2h5c3ed"
C = "aaabbceedd"  # == "a3b2ce2d2"
D = "abcde"  # == "abcde"
E = "aaabbdefffff"  # == "a3b2def5"

ALL_STRINGS = [A, B, C, D, E]


def count_char(text: str) -> str:
    """Count consecutive characters in a string.
    """
    a = ["".join(group) for _, group in groupby(text)]
    numbers = [len(item) for item in a]
    letters = [item[0] for item in a]
    combo = zip(letters, numbers)
    return ''.join([f"{i}{j}" for i, j in combo]).replace('1', '')


if __name__ == '__main__':

    for string in ALL_STRINGS:
        print(count_char(string))
