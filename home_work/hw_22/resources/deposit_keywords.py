import logging

from robot.api.deco import keyword
from home_work.hw_11.bank_deposit.deposit import Deposit

logger = logging.getLogger(__name__)


@keyword
def create_deposit(initial_investment, years, interest_rate=None):
    initial_investment = float(initial_investment)
    years = int(years)
    if interest_rate is not None:
        interest_rate = float(interest_rate)
        return Deposit(initial_investment, years, interest_rate)
    return Deposit(initial_investment, years)


@keyword
def get_initial_investment(deposit):
    return deposit.initial_investment


@keyword
def get_investment_length(deposit):
    return deposit.investment_len_in_years


@keyword
def get_interest_rate(deposit):
    return deposit.interest_rate


@keyword
def calculate_final_amount(deposit):
    return deposit.calculate_final_amount()


@keyword
def log_message(message):
    logger.info(message)
