import random
import sys
from card import Card

CHOOSE_CARD_TEXT_EN = 'Choose a card from the deck (from 1 to {}):\n> '
ERROR_LEN_DECK = 'Error: enter a card number from 1 to {}'
ERROR_INPUT_NOT_INT = 'Error: enter an integer.'


class CardsDeck:
    def __init__(self):
        self.cards = [Card(number, mast) for mast in Card.mast_list for number in Card.number_list]
        self.cards += [Card(number, mast) for number, mast in Card.joker_list]

    def shuffle(self):
        random.shuffle(self.cards)

    def get_card(self):
        card_number = self._input_card_number()
        if card_number is not None:
            self.cards.pop(card_number).show_card()

    def show_remaining_cards(self):
        for i, card in enumerate(self.cards):
            print(f"{i + 1}: {card}")

    def _card_validator(self, card_num):
        if 0 <= card_num < len(self.cards):
            return card_num
        else:
            print(ERROR_LEN_DECK.format(len(self.cards)))
            return None

    def _input_card_number(self):
        while True:
            try:
                card_num = int(input(CHOOSE_CARD_TEXT_EN.format(len(self.cards)))) - 1

                # EXIT: If User Input == -100 or Card Deck is Empty
                if card_num + 1 == -100 or not len(self.cards):
                    sys.exit()

                if valid_card_num := self._card_validator(card_num) is not None:
                    return valid_card_num

            except ValueError:
                print(ERROR_INPUT_NOT_INT)
