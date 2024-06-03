"""Module for type-based decorator."""


def typed(type_):
    """Decorator factory to enforce argument types."""

    def real_decorator(func):
        """Real decorator to enforce argument types."""

        def wrapper(*args, **kwargs):
            """Wrapper function to enforce argument types."""
            args = [type_(arg) for arg in args]
            kwargs = {k: type_(v) for k, v in kwargs.items()}
            return func(*args, **kwargs)

        return wrapper

    return real_decorator


@typed(type_=str)
def add_str(a, b):
    """Concatenate two strings."""
    return a + b


@typed(type_=int)
def add_int(a, b, c):
    """Add three integers."""
    return a + b + c


@typed(type_=float)
def add_float(a, b, c):
    """Add three floating point numbers."""
    return a + b + c


assert add_str("3", 5) == '35', \
    f"Expected '35', got {add_str('3', 5)}"

assert add_str(5, 5) == '55', \
    f"Expected '55', got {add_str(5, 5)}"

assert add_str('a', 'b') == 'ab', \
    f"Expected 'ab', got {add_str('a', 'b')}"

assert add_int(5, 6, 7) == 18, \
    f"Expected 18, got {add_int(5, 6, 7)}"

assert add_float(0.1, 0.2, 0.4) == 0.7000000000000001, \
    f"Expected 0.7000000000000001, got {add_float(0.1, 0.2, 0.4)}"
