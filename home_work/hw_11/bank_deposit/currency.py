import os
import requests
from dotenv import load_dotenv
from home_work.hw_11.bank_deposit.currency_enum import Currency

from log_.logging_setup import get_logger

log = get_logger(__name__)

load_dotenv()

API_KEY = os.getenv('API_KEY')
BASE_URL = "https://v6.exchangerate-api.com/v6/"
BASE_CURRENCY = Currency.USD
URL = f"{BASE_URL}{API_KEY}/latest/{BASE_CURRENCY}"
HEADERS = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {API_KEY}'
}


class CurrencyConverter:

    @staticmethod
    def _get_exchange_rates():

        response = requests.get(URL, headers=HEADERS, timeout=5)
        response.raise_for_status()
        return response.json()['conversion_rates']

    @staticmethod
    def convert(from_curr: str,
                amount: int,
                to_curr: str = 'BYN',
                round_to: int = 2):

        rates = CurrencyConverter._get_exchange_rates()

        if from_curr not in rates:
            log.error(f"Unsupported currency: {from_curr}")
            return False
        elif to_curr not in rates:
            log.error(f"Unsupported currency: {to_curr}")
            return False
        else:
            amount_in_usd_base_currency = amount / rates[from_curr]
            converted = round(amount_in_usd_base_currency * rates[to_curr], round_to)

        return converted, to_curr
