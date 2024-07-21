import pytest
import logging
from home_work.hw_11.bank_deposit.bank import Bank

logger = logging.getLogger(__name__)


@pytest.fixture
def bank():
    return Bank()


@pytest.fixture
def registered_bank(bank):
    client_id = 1
    client_name = "Pikachu"
    bank.register_client(client_id, client_name)
    return bank, client_id, client_name


def test_register_client_positive(bank):
    client_id = 1
    client_name = "Pikachu"
    logger.info('Test 1: Register a client successfully')
    bank.register_client(client_id, client_name)
    assert client_id in bank.clients
    assert bank.clients[client_id] == client_name


def test_register_client_negative_already_registered(registered_bank):
    bank, client_id, client_name = registered_bank
    logger.info('Test 2: Try to register an already registered client')
    assert not bank.register_client(client_id, client_name)


def test_open_deposit_account_positive(registered_bank):
    bank, client_id, _ = registered_bank
    logger.info('Test 3: Open a deposit account successfully')
    bank.open_deposit_account(client_id, 1000, 1)
    assert client_id in bank.deposits


def test_open_deposit_account_negative_not_registered(bank):
    logger.info('Test 4: Try to open a deposit account for a not registered client')
    assert not bank.open_deposit_account(1, 1000, 1)


def test_open_deposit_account_negative_already_has_deposit(registered_bank):
    bank, client_id, _ = registered_bank
    logger.info('Test 5: Try to open a second deposit account for a client')
    assert bank.open_deposit_account(client_id, 1000, 1)
    assert not bank.open_deposit_account(client_id, 1000, 1)


def test_calc_interest_rate_positive(registered_bank):
    bank, client_id, _ = registered_bank
    logger.info('Test 6: Calculate interest rate successfully')
    bank.open_deposit_account(client_id, 1000, 1)
    interest = bank.calc_interest_rate(client_id)
    assert interest is not None


def test_calc_interest_rate_negative_not_registered(bank):
    logger.info('Test 7: Try to calculate interest rate for a not registered client')
    interest = bank.calc_interest_rate(1)
    assert interest is None


def test_calc_interest_rate_negative_no_deposit(registered_bank):
    bank, client_id, _ = registered_bank
    logger.info('Test 8: Try to calculate interest rate for a client without a deposit')
    interest = bank.calc_interest_rate(client_id)
    assert interest is None


def test_close_deposit_positive(registered_bank):
    bank, client_id, _ = registered_bank
    logger.info('Test 9: Close a deposit account successfully')
    assert bank.open_deposit_account(client_id, 1000, 1)
    assert bank.close_deposit(client_id)


def test_close_deposit_negative_not_registered(bank):
    logger.info('Test 10: Try to close a deposit for a not registered client')
    result = bank.close_deposit(1)
    assert result is None


def test_close_deposit_negative_no_deposit(registered_bank):
    bank, client_id, _ = registered_bank
    logger.info('Test 11: Try to close a deposit for a client without a deposit')
    result = bank.close_deposit(client_id)
    assert result is None
