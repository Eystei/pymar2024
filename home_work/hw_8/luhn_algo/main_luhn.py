"""
This module is the main script to test the Luhn algorithm implementation.
"""

from home_work.hw_8.luhn_algo.cards_data import cards
from home_work.hw_8.luhn_algo.luhn_algo import LuhnAlgorithm

if __name__ == '__main__':

    for name, card_number in cards.items():
        card_number = str(card_number)

        if not LuhnAlgorithm.validator_all_digits(card_number):
            print(f"Error: must contain only digits, but {card_number}")
            continue

        result = str(LuhnAlgorithm.verify(card_number))

        print(f"{result.ljust(6)}|{name.rjust(26)} | {card_number}")
