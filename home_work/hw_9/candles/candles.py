"""
Module for burning candles.
"""

ERROR_MSG = "Expected {} candles to be burned"


def burn_candles(candles, candles_end):
    """
    Calculate the total number of candles burned.
    """

    fired_candles = candles

    while candles >= candles_end:
        new_candles = int(candles / candles_end)
        fired_candles += new_candles
        candles = new_candles + (candles % candles_end)
    return fired_candles


assert burn_candles(5, 2) == 9, ERROR_MSG.format("9")
assert burn_candles(1, 2) == 1, ERROR_MSG.format("1")
assert burn_candles(15, 5) == 18, ERROR_MSG.format("18")
assert burn_candles(12, 2) == 23, ERROR_MSG.format("23")
assert burn_candles(6, 4) == 7, ERROR_MSG.format("7")
assert burn_candles(13, 5) == 16, ERROR_MSG.format("16")
assert burn_candles(2, 3) == 2, ERROR_MSG.format("2")
