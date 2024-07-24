from home_work.hw_11.bank_deposit.currency import CurrencyConverter
from home_work.hw_11.bank_deposit.deposit import Deposit
import logging

logger = logging.getLogger(__name__)


class Bank:
    __slots__ = ('clients', 'deposits')

    def __init__(self):
        self.clients = {}
        self.deposits = {}

    def register_client(self, client_id, name):
        if client_id not in self.clients:
            self.clients[client_id] = name
            self.deposits[client_id] = None
            logger.info(f'Client registered. id: {client_id}')
            return True
        else:
            logger.warning(f'Client {client_id} already registered')
            return False

    def open_deposit_account(self, client_id, start_balance, years):
        if client_id not in self.clients:
            logger.warning(f"Client {client_id} not registered")
            return False
        elif self.deposits[client_id] is not None:
            logger.warning(f"Client {client_id} already has a deposit")
            return False
        else:
            self.deposits[client_id] = Deposit(
                initial_investment=start_balance,
                investment_in_years=years
            )
            logger.info(f"Deposit has created for client id: {client_id}")
            return True

    def calc_interest_rate(self, client_id):
        if client_id not in self.clients:
            logger.warning('Client not registered')
            return None
        elif self.deposits[client_id] is None:
            logger.warning("Client doesn't have a deposit")
            return None
        else:
            return self.deposits[client_id].calculate_final_amount()

    def close_deposit(self, client_id):
        if client_id not in self.clients:
            logger.warning('Client not registered')
            return None
        elif self.deposits[client_id] is None:
            logger.warning("Client doesn't have a deposit")
            return None
        else:
            total = self.calc_interest_rate(client_id)
            self.deposits[client_id] = None
            logger.info(f"Client id: {client_id} close deposit. {total}")
            return total

    @staticmethod
    def exchange_currency(from_curr, amount, to_curr='BYN'):

        from_curr = from_curr.upper()
        to_curr = to_curr.upper()

        converted, target_curr = CurrencyConverter.convert(from_curr, amount, to_curr)

        if not converted:
            logger.error("Conversion failed")
            return False

        logger.info(f"Converted {amount} {from_curr} to {converted} {target_curr}")
        return converted, converted
