"""
Module for Bulls and Cows game implementation.
"""

import random
import string


# pylint: disable=too-few-public-methods
class BullsAndCows:
    """Bulls and Cows game implementation."""

    def __init__(self):
        """Initializes a new instance of the BullsAndCows class."""
        self.secret_number = "".join(random.sample(string.digits, 4))

    def check_guess(self, guess):
        """
        Checks the guess against the secret number and returns
        the number of bulls and cows.
        """

        bulls = 0
        cows = 0
        for i in range(4):
            if guess[i] == self.secret_number[i]:
                bulls += 1
            elif guess[i] in self.secret_number:
                cows += 1

        return bulls, cows
