import requests
from loguru import logger as log

API_KEY = '1240d98b1bc1385eea7ad602'
API_URL = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/USD"


class CurrencyConverter:

    @classmethod
    def _get_exchange_rates(cls):

        response = requests.get(API_URL, timeout=5)
        response.raise_for_status()
        return response.json()['conversion_rates']

    @classmethod
    def convert(cls,
                from_curr: str,
                amount: int,
                to_curr: str = 'BYN',
                round_to: int = 2):

        rates = cls._get_exchange_rates()

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
