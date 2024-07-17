import pytest
from log_.logging_setup import get_logger
from home_work.hw_11.bank_deposit.deposit import Deposit

logger = get_logger(__name__)


def test_initial_investment():
    logger.test('Test 1: Validate initial investment is stored correctly')
    deposit = Deposit(1000, 1)
    assert deposit.initial_investment == 1000


def test_investment_length():
    logger.test('Test 2: Validate investment length is stored correctly')
    deposit = Deposit(1000, 1)
    assert deposit.investment_len_in_years == 1


def test_default_interest_rate():
    logger.test('Test 3: Ensure default interest rate is used when not specified')
    deposit = Deposit(1000, 1)
    assert deposit.interest_rate == 0.10


def test_custom_interest_rate():
    logger.test('Test 4: Validate that a custom interest rate is stored correctly')
    deposit = Deposit(1000, 1, 0.05)
    assert deposit.interest_rate == 0.05


def test_calculate_final_amount():
    logger.test('Test 5: Check correct calculation of the final amount')
    deposit = Deposit(1000, 1, 0.10)
    monthly_rate = 0.10 / 12
    months = 1 * 12
    expected_final_amount = 1000 * (1 + monthly_rate) ** months
    assert round(deposit.calculate_final_amount(), 2) == round(expected_final_amount, 2)


def test_negative_initial_investment():
    logger.test('Test 6: Test with negative initial investment')
    with pytest.raises(ValueError):
        Deposit(-1000, 1)


def test_zero_years_investment():
    logger.test('Test 7: Test with zero years of investment')
    deposit = Deposit(1000, 0)
    assert deposit.calculate_final_amount() == 1000
