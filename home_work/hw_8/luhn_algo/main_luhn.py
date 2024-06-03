"""
This module is the main script to test the Luhn algorithm implementation.
"""

import json

from home_work.hw_8.luhn_algo.luhn_algo import validator_all_digits, verify

with open('cards_data.json', 'r', encoding='utf-8') as file:
    cards_dict = json.load(file)

for name, card_number in cards_dict.items():
    card_number_str = str(card_number)

    if not validator_all_digits(card_number_str):
        print(f"Error: must contain only digits, but {card_number_str}")
        continue

    result_str = str(verify(card_number_str))

    print(f"{result_str.ljust(6)}|{name.rjust(26)} | {card_number_str}")
