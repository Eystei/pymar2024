import unittest
import logging


from home_work.hw_11.bank_deposit.deposit import Deposit
logger = logging.getLogger(__name__)


class TestDeposit(unittest.TestCase):
    def test_initial_investment(self):
        logger.info('Test 1: Validate initial investment is stored correctly')
        deposit = Deposit(1000, 1)
        self.assertEqual(deposit.initial_investment, 1000)

    def test_investment_length(self):
        logger.info('Test 2: Validate investment length is stored correctly')
        deposit = Deposit(1000, 1)
        self.assertEqual(deposit.investment_len_in_years, 1)

    def test_default_interest_rate(self):
        logger.info('Test 3: Ensure default interest rate is used when not specified')
        deposit = Deposit(1000, 1)
        self.assertEqual(deposit.interest_rate, 0.10)

    def test_custom_interest_rate(self):
        logger.info('Test 4: Validate that a custom interest rate is stored correctly')
        deposit = Deposit(1000, 1, 0.05)
        self.assertEqual(deposit.interest_rate, 0.05)

    def test_calculate_final_amount(self):
        logger.info('Test 5: Check correct calculation of the final amount')
        deposit = Deposit(1000, 1, 0.10)
        monthly_rate = 0.10 / 12
        months = 1 * 12
        expected_final_amount = 1000 * (1 + monthly_rate) ** months
        self.assertAlmostEqual(deposit.calculate_final_amount(), round(expected_final_amount, 2))

    def test_negative_initial_investment(self):
        logger.info('Test 6: Test with negative initial investment')
        with self.assertRaises(ValueError):
            Deposit(-1000, 1)

    def test_zero_years_investment(self):
        logger.info('Test 7: Test with zero years of investment')
        deposit = Deposit(1000, 0)
        self.assertEqual(deposit.calculate_final_amount(), 1000)


if __name__ == "__main__":
    unittest.main()
