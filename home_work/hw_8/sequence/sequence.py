"""
This module provides a function to check if a given sequence
is strictly increasing sequence
"""


def solution(seq):
    """Defines a strictly increasing sequence by removing
     at most one element from the list.
    """
    temp = []
    i = 0

    if len(seq) == 1:
        return True

    if seq[0] >= seq[1]:
        temp.append(seq.pop(0))

    while i < len(seq) - 1:

        if seq[i] >= seq[i + 1]:
            temp.append(seq.pop(i + 1))
        else:
            i += 1

    return len(temp) <= 1


assert solution([1]), "Expected True in sequence [1]"
assert solution([1, 2, 3]), "Expected True in sequence [1, 2, 3]"
assert solution([3, 1, 2, 3]), "Expected True in sequence [3, 1, 2, 3]"

assert not solution([1, 2, 1, 2]), "Expected False in sequence [1, 2, 1, 2]"
assert not solution([1, 3, 2, 1]), "Expected False in sequence [1, 3, 2, 1]"
assert not solution([1, 2, 1, 2]), "Expected False in sequence [1, 2, 1, 2]"
assert not solution([1, 2, 3, 4, 5, 3, 5, 6]), \
    "Expected False in sequence [1, 2, 3, 4, 5, 3, 5, 6]"
assert not solution([40, 50, 60, 10, 20, 30]), \
    "Expected False in sequence [40, 50, 60, 10, 20, 30]"
