"""
Module for Bulls and Cows game implementation.
"""

import random
import string


class BullsAndCows:
    """Bulls and Cows game implementation."""

    def __init__(self):
        """Initializes a new instance of the BullsAndCows class."""
        self.secret_number = self.gen_four_digit_num()

    @staticmethod
    def gen_four_digit_num():
        """Generates a random four-digit number."""
        return "".join(random.sample(string.digits, 4))

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

            if guess[i] in self.secret_number:
                cows += 1

        return bulls, cows
