"""
Module for removing characters followed by a hash sign.
"""

A = "a#bc#d"  # ==>  "bd"
B = "abc#d##c"  # ==>  "ac"
C = "abc##d######"  # ==>  ""
D = "#######"  # ==>  ""
E = ""  # ==>  ""


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


def process_string(str_: str) -> str:
    """Process the string according to specified rules."""
    if all(char == '#' for char in str_) or not str_:
        return ''
    return remove_char_with_next_hash_sign(str_)


assert process_string(A) == "bd", "Expected 'bd'"
assert process_string(B) == "ac", "Expected 'ac'"
assert process_string(C) == "", "Expected: empty string"
assert process_string(D) == "", "Expected: empty string"
assert process_string(E) == "", "Expected: empty string"
