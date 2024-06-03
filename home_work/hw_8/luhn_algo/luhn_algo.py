"""
This module implements the Luhn algorithm for validating credit card numbers.
"""
import re


def validator_checksum(card_number: str) -> int:
    """
    Compute the Luhn checksum for the provided string of digits. Note this
    assumes the check digit is in place.
    """
    digits = [int(digit) for digit in str(card_number)]
    odd_sum = sum(digits[-1::-2])
    even_sum = sum(sum(divmod(2 * d, 10)) for d in digits[-2::-2])
    return (odd_sum + even_sum) % 10


def verify(card_number: str) -> int:
    """
    Check if the provided string of digits satisfies the Luhn checksum.
    """
    return validator_checksum(card_number) == 0


def validator_all_digits(number: str) -> bool:
    """Check if the provided string contain only digits."""

    return re.match(r'^\d+$', str(number)) is not None
