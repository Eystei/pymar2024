"""Module for type-based decorator."""
import loguru


def typed(type_):
    """Decorator factory to enforce argument types."""

    def real_decorator(func):
        """Real decorator to enforce argument types."""

        def wrapper(*args, **kwargs):
            """Wrapper function to enforce argument types."""
            args = [arg if isinstance(arg, type_) else type_(arg) for arg in args]
            kwargs = {k: v if isinstance(v, type_) else type_(v) for k, v in kwargs.items()}

            return func(*args, **kwargs)

        return wrapper

    return real_decorator


@typed(type_=str)
def add_str(*args, **kwargs):
    """Concatenate multiple strings."""
    return ''.join(args) + ''.join(kwargs.values())


@typed(type_=int)
def add_int(*args, **kwargs):
    """Add integers."""
    return sum(args) + sum(kwargs.values())


@typed(type_=float)
def add_float(*args, **kwargs):
    """Add floating point numbers."""
    return sum(args) + sum(kwargs.values())


assert add_str("3", 5) == '35', \
    f"Expected '35', got {add_str('3', 5)}"

assert add_str(5, 5) == '55', \
    f"Expected '55', got {add_str(5, 5)}"

assert add_str('a', 'b') == 'ab', \
    f"Expected 'ab', got {add_str('a', 'b')}"

assert add_int(5, "6", 7) == 18, \
    f"Expected 18, got {add_int(5, 6, 7)}"

assert add_float(0.1, 0.2, 0.4) == 0.7000000000000001, \
    f"Expected 0.7000000000000001, got {add_float(0.1, 0.2, 0.4)}"


##########################################################################
# For Sergey Stamal
# Why we should use decorator for typing if solution below seems more
# flexible. Without uses any decorators.

def add(type_, *args, **kwargs):
    """   Converts all positional and keyword arguments to the specified type,
    then concatenates them or sums.
    """

    args = [arg if isinstance(arg, type_) else type_(arg) for arg in args]
    kwargs = {k: v if isinstance(v, type_) else type_(v) for k, v in kwargs.items()}

    if type_ == str:
        return ''.join(args) + ''.join(kwargs.values())
    elif type_ in [int, float]:
        return sum(args) + sum(kwargs.values())
    else:
        loguru.logger.error("Function support only str | float | int")
        raise TypeError("Function support only str | float | int")


assert add(str, "3", 5) == '35', \
    f"Expected '35', got {add('3', 5)}"

assert add(str, 5, 5) == '55', \
    f"Expected '55', got {add(5, 5)}"

assert add(str, 'a', 'b') == 'ab', \
    f"Expected 'ab', got {add('a', 'b')}"

assert add(int, 5, "6", 7) == 18, \
    f"Expected 18, got {add(5, 6, 7)}"

assert add(float, 0.1, 0.2, 0.4) == 0.7000000000000001, \
    f"Expected 0.7000000000000001, got {add(0.1, 0.2, 0.4)}"
