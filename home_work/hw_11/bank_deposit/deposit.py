MONTHS_IN_YEAR = 12
INTEREST_RATE_DEFAULT = 0.10


class Deposit:
    def __init__(self,
                 initial_investment: int,
                 investment_in_years: int,
                 interest_rate: float | int = INTEREST_RATE_DEFAULT):

        self.initial_investment = initial_investment
        self.investment_len_in_years = investment_in_years
        self.interest_rate = interest_rate

    def calculate_final_amount(self):
        """Calculates the final amount after the investment period.

        total  = initial_investment * (1 + (interest_rate / 12)) ** (investment_in_years * 12)
        """

        monthly_rate = self.interest_rate / MONTHS_IN_YEAR
        months = self.investment_len_in_years * MONTHS_IN_YEAR
        ending_balance = self.initial_investment * (1 + monthly_rate) ** months
        return round(ending_balance, 2)


def calc_end_balance(depo: Deposit):
    """ Calculates the final amount of a deposit."""

    return depo.calculate_final_amount()
