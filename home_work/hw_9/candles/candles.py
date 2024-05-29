"""
Module for burning candles.
"""


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


if __name__ == '__main__':
    print(burn_candles(5, 2))
    print(burn_candles(1, 2))
    print(burn_candles(15, 5))
    print(burn_candles(12, 2))
    print(burn_candles(6, 4))
    print(burn_candles(13, 5))
    print(burn_candles(2, 3))

    assert burn_candles(5, 2) == 9
    assert burn_candles(1, 2) == 1
    assert burn_candles(15, 5) == 18
    assert burn_candles(12, 2) == 23
    assert burn_candles(6, 4) == 7
    assert burn_candles(13, 5) == 16
    assert burn_candles(2, 3) == 2
