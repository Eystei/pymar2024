"""
This module contains decorators for validating string params
"""


def validate_string_type(func):
    """Decorator to ensure that
    the argument passed to the decorated function is of type string.
    """
    def wrapper(text):
        assert isinstance(text, str), f"Argument in function '{func.__name__}' must be a string."
        return func(text)

    return wrapper


def validate_string_is_not_empty(func):
    """Decorator to ensure that
    the argument passed to the decorated function is not an empty string.
    """
    def wrapper(text):
        assert text.strip(), "Length of text must be greater than 0"
        return func(text)

    return wrapper
