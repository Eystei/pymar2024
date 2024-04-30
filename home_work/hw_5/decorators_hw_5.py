"""
This module contains decorators for validating string params
"""


def validate_string_type(func):
    def wrapper(text):
        assert isinstance(text, str), f"Argument in function '{func.__name__}' must be a string."
        return func(text)

    return wrapper


def validate_string_is_not_empty(func):
    def wrapper(text):
        assert text.strip(), "Length of text must be greater than 0"
        return func(text)

    return wrapper
