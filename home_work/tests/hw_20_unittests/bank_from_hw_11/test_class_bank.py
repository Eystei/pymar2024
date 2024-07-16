import unittest
from log_.logging_setup import get_logger
from home_work.hw_11.bank_deposit.bank import Bank


logger = get_logger(__name__)


class TestBank(unittest.TestCase):
    CLIENT_NAME = "Pikachu"

    def setUp(self):
        self.bank = Bank()

    def test_register_client_positive(self):
        logger.test('Test 1: Register a client successfully')
        self.bank.register_client(1, self.CLIENT_NAME)
        self.assertIn(1, self.bank.clients)
        self.assertEqual(self.bank.clients[1], self.CLIENT_NAME)

    def test_register_client_negative_already_registered(self):
        logger.test('Test 2: Try to register an already registered client')
        self.bank.register_client(1, self.CLIENT_NAME)
        with self.assertLogs(level='WARNING') as log:
            self.bank.register_client(1, self.CLIENT_NAME)
        self.assertIn('already registered', log.output[0])

    def test_open_deposit_account_positive(self):
        logger.test('Test 3: Open a deposit account successfully')
        self.bank.register_client(1, self.CLIENT_NAME)
        self.bank.open_deposit_account(1, 1000, 1)
        self.assertIsNotNone(self.bank.deposits[1])

    def test_open_deposit_account_negative_not_registered(self):
        logger.test('Test 4: Try to open a deposit account for a not registered client')
        with self.assertLogs(level='WARNING') as log:
            self.bank.open_deposit_account(1, 1000, 1)
        self.assertIn('not registered', log.output[0])

    def test_open_deposit_account_negative_already_has_deposit(self):
        logger.test('Test 5: Try to open a second deposit account for a client')
        self.bank.register_client(1, self.CLIENT_NAME)
        self.bank.open_deposit_account(1, 1000, 1)
        with self.assertLogs(level='WARNING') as log:
            self.bank.open_deposit_account(1, 1000, 1)
        self.assertIn('already has a deposit', log.output[0])

    def test_calc_interest_rate_positive(self):
        logger.test('Test 6: Calculate interest rate successfully')
        self.bank.register_client(1, self.CLIENT_NAME)
        self.bank.open_deposit_account(1, 1000, 1)
        interest = self.bank.calc_interest_rate(1)
        self.assertIsNotNone(interest)

    def test_calc_interest_rate_negative_not_registered(self):
        logger.test('Test 7: Try to calculate interest rate for a not registered client')
        interest = self.bank.calc_interest_rate(1)
        self.assertIsNone(interest)

    def test_calc_interest_rate_negative_no_deposit(self):
        logger.test('Test 8: Try to calculate interest rate for a client without a deposit')
        self.bank.register_client(1, self.CLIENT_NAME)
        interest = self.bank.calc_interest_rate(1)
        self.assertIsNone(interest)

    def test_close_deposit_positive(self):
        logger.test('Test 9: Close a deposit account successfully')
        self.bank.register_client(1, self.CLIENT_NAME)
        self.bank.open_deposit_account(1, 1000, 1)
        result = self.bank.close_deposit(1)
        self.assertIsNotNone(result)
        self.assertIsNone(self.bank.deposits[1])

    def test_close_deposit_negative_not_registered(self):
        logger.test('Test 10: Try to close a deposit for a not registered client')
        result = self.bank.close_deposit(1)
        self.assertIsNone(result)

    def test_close_deposit_negative_no_deposit(self):
        logger.test('Test 11: Try to close a deposit for a client without a deposit')
        self.bank.register_client(1, self.CLIENT_NAME)
        result = self.bank.close_deposit(1)
        self.assertIsNone(result)


if __name__ == "__main__":
    unittest.main()
