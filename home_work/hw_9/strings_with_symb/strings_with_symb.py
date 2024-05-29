"""
Module for removing characters followed by a hash sign.
"""

A = "a#bc#d"  # ==>  "bd"
B = "abc#d##c"  # ==>  "ac"
C = "abc##d######"  # ==>  ""
D = "#######"  # ==>  ""
E = ""  # ==>  ""

ALL_STRINGS = [A, B, C, D, E]


def remove_char_with_next_hash_sign(text: str) -> str:
    """    Remove characters followed by a hash sign from the text.
    """
    i = 0
    while i < len(text) - 1:
        if text[i + 1] == '#':
            text = text[:i] + text[i + 2:]
            if i > 0:
                i -= 1
        else:
            i += 1
    return text


if __name__ == '__main__':
    for string in ALL_STRINGS:
        if all(char == '#' for char in string) or not string:
            print('')
        else:
            print(remove_char_with_next_hash_sign(string))
