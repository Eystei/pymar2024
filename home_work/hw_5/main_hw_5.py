"""
This module contain solution for HW#5
"""

# - Заменить символ “#” на символ “/” в строке 'www.my_site.com#about'
# - Напишите программу, которая добавляет ‘ing’ к словам
# - В строке “Ivanou Ivan” поменяйте местами слова => "Ivan Ivanou"
# - Напишите программу, которая удаляет пробел в начале, в конце строки
#
# После выполнения домашнего задания, зафиксируйте свои изменения и сделайте PR,
# так же как вы это делали в ДЗ по Git


SOME_TEXT_1 = 'www.my_site.com#about'
SOME_TEXT_2 = 'Pasting anything in here could give attackers access to your Discord account'
TWO_WORDS = 'Ivanou Ivan'
TEXT_WITH_SPACES = "   String without trailing spaces   "


def replace_hash_sign_on_slash_sign(*, text: str) -> str:
    """ Replaces the '#' symbol with the '/' symbol in the given text. """

    assert isinstance(text, str), "Argument 'string' must be a string."
    assert text, "Length of text must be greater than 0"

    if "#" in text:
        return text.replace("#", "/")

    return text


def add_ing_to_words(text: str) -> str:
    """Adds 'ing' to words"""

    assert isinstance(text, str), "Argument 'string' must be a string."
    assert text, "Length of text must be greater than 0"
    words = text.split(" ")

    return " ".join([f"{item}ing" for item in words])


def swap_two_words(words: str) -> str:
    """Swaps the positions of two words in a sentence."""

    assert isinstance(words, str), "Argument 'string' must be a string."
    words = words.split(" ")
    assert len(words) == 2, "The input sentence must contain exactly two words."

    return f"{words[1]} {words[0]}"


def remove_trailing_spaces(text: str) -> str:
    """ Removes leading and trailing spaces from a string. """
    assert isinstance(text, str), "Argument 'string' must be a string."
    assert text, "Length of text must be greater than 0"

    return text.strip()


if __name__ == '__main__':
    print(replace_hash_sign_on_slash_sign(text=SOME_TEXT_1))
    print(add_ing_to_words(text=SOME_TEXT_2))
    print(swap_two_words(words=TWO_WORDS))
    print(remove_trailing_spaces(text=TEXT_WITH_SPACES))
