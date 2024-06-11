from loguru import logger as log

from home_work.hw_11.bank_deposit.deposit import Deposit


class Bank:
    __slots__ = ('clients', 'deposits')

    def __init__(self):
        self.clients = {}
        self.deposits = {}

    def register_client(self, client_id, name):
        if client_id not in self.clients:
            self.clients[client_id] = name
            self.deposits[client_id] = None
            log.success(f'Client registered. id: {client_id}')
        else:
            log.warning(f'Client {client_id} already registered')

    def open_deposit_account(self, client_id, start_balance, years):
        if client_id not in self.clients:
            log.warning(f"Client {client_id} not registered")
        elif self.deposits[client_id] is not None:
            log.warning(f"Client {client_id} already has a deposit")
        else:
            self.deposits[client_id] = Deposit(
                initial_investment=start_balance,
                investment_in_years=years
            )
            log.success(f"Deposit has created for client id: {client_id}")

    def calc_interest_rate(self, client_id):
        if client_id not in self.clients:
            log.warning('Client not registered')
        elif self.deposits[client_id] is None:
            log.warning("Client doesn't have a deposit")
        else:
            return self.deposits[client_id].calculate_final_amount()

    def close_deposit(self, client_id):
        if client_id not in self.clients:
            log.warning('Client not registered')
        elif self.deposits[client_id] is None:
            log.warning("Client doesn't have a deposit")
        else:
            total = self.calc_interest_rate(client_id)
            self.deposits[client_id] = None
            log.success(f"Client id: {client_id} close deposit. {total}")
            return total
