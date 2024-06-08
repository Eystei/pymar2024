from functools import lru_cache

from loguru import logger


def cache(func):
    cache_storage = {}

    def wrapper(arg):
        if arg in cache_storage:
            logger.debug(f'def {func.__name__} | {arg} Received from cache')
            return cache_storage[arg]
        else:
            result = func(arg)
            cache_storage[arg] = result
            return result

    return wrapper


@cache
def fibonacci_1(n):
    if n <= 1:
        return n
    return fibonacci_1(n - 1) + fibonacci_1(n - 2)


assert fibonacci_1(7) == 13
assert fibonacci_1(10) == 55
assert fibonacci_1(7) == 13


@lru_cache
def fibonacci_2(n):
    if n <= 1:
        return n
    return fibonacci_2(n - 1) + fibonacci_2(n - 2)


assert fibonacci_2(7) == 13
assert fibonacci_2(10) == 55
assert fibonacci_2(7) == 13

logger.success(f"def fibonacci_2 | {fibonacci_2.cache_info()}")
