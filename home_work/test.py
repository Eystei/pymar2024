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


if __name__ == '__main__':
    print(solution([1]))
    print(solution([1, 2, 3]))
    print(solution([1, 2, 1, 2]))
    print(solution([3, 1, 2, 3]))
    print(solution([1, 3, 2, 1]))
    print(solution([1, 2, 1, 2]))
    print(solution([1, 2, 3, 4, 5, 3, 5, 6]))
    print(solution([40, 50, 60, 10, 20, 30]))
