"""Module for validating return value as number."""


from loguru import logger


def validate_result_is_number(func):
    """Decorator function to validate the result is a number."""
    def wrapper(*args, **kwargs):
        """Wrapper function to validate the result is a number."""
        res = func(*args, **kwargs)

        if not isinstance(res, (int, float)):
            logger.error(f"ERROR: The return value ('{res}') of the function "
                         f"'{func.__name__}()' is not a number, but {type(res)}.")

        return res

    return wrapper


@validate_result_is_number
def concat_str(a, b):
    """Concatenate two strings."""
    return f"{a} {b}"


@validate_result_is_number
def summ(*args, **kwargs):
    """Sum numeric values."""
    return sum(args) + sum(kwargs.values())


assert summ(-1, 2) == 1
assert summ(a=1.2, b=0) == 1.2
concat_str('foo', 'bar')
