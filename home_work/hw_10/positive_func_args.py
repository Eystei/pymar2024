"""Module for validating function arguments."""


def validate_arguments(func):
    """Decorator function to validate arguments."""
    def wrapper(*args, **kwargs):
        """Wrapper function to validate arguments."""
        for i in args:
            if i < 1:
                raise ValueError(f"{i} is not a positive")

        for v in kwargs.values():
            if v < 1:
                raise ValueError(f"{v} is not a positive")

        return func(*args, **kwargs)

    return wrapper


@validate_arguments
def summ(*args, **kwargs):
    """Function to sum arguments after validation."""
    return sum(args) + sum(kwargs.values())


assert summ(1, 1, 1, 1, a=1, b=1) == 6, "Expected 6 for the sum of args"
assert summ(5, b=3, c=2) == 10, "Expected 10 for the sum of args"
assert summ(b=3, c=2) == 5, "Expected 5 for the sum of args"
