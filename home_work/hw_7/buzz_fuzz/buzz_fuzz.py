"""
Module for the BuzzFuzz game implementation.
"""


def buzzfuzz(num=100):
    """   Prints
    'Fuzz' for numbers divisible by 3, 'Buzz' for numbers divisible by 5,
    'FuzzBuzz' for numbers divisible by both 3 and 5,
    and the number itself for all other numbers.
    """
    for i in range(1, num + 1):
        print("Fuzz" * (i % 3 == 0) + "Buzz" * (i % 5 == 0) or i)


if __name__ == "__main__":
    buzzfuzz()
