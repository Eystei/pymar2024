class Card:
    number_list = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
    mast_list = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    joker_list = [('Joker', 'Black'), ('Joker', 'Red')]

    def __init__(self, number, mast=None):
        self.number = number
        self.mast = mast

    def __str__(self):
        return f'{self.mast} {self.number}'

    def show_card(self):
        print(f'{self.mast} {self.number}')
