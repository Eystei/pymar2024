from home_work.hw_12.card_deck.cards_deck import CardsDeck


def main():
    deck = CardsDeck()

    deck.shuffle()

    deck.show_remaining_cards()

    deck.get_card()
    deck.get_card()
    deck.get_card()

    deck.show_remaining_cards()

    deck.shuffle()

    deck.show_remaining_cards()

    deck.get_card()

    deck.show_remaining_cards()


if __name__ == "__main__":
    main()
