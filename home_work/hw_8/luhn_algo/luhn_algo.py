"""
This module implements the Luhn algorithm for validating credit card numbers.
"""
import re


class LuhnAlgorithm:
    """
    A class used to represent the Luhn Algorithm for credit card validation.
    """

    @staticmethod
    def validator_checksum(card_number: str) -> int:
        """
        Compute the Luhn checksum for the provided string of digits. Note this
        assumes the check digit is in place.
        """
        digits = [int(digit) for digit in str(card_number)]
        odd_sum = sum(digits[-1::-2])
        even_sum = sum(sum(divmod(2 * d, 10)) for d in digits[-2::-2])
        return (odd_sum + even_sum) % 10

    @staticmethod
    def verify(card_number: str) -> int:
        """
        Check if the provided string of digits satisfies the Luhn checksum.
        """
        return LuhnAlgorithm.validator_checksum(card_number) == 0

    @staticmethod
    def validator_all_digits(number: str) -> bool:
        """Check if the provided string contain only digits."""

        return re.match(r'^\d+$', str(number)) is not None
