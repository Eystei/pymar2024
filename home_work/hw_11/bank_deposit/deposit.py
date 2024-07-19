MONTHS_IN_YEAR = 12
INTEREST_RATE_DEFAULT = 0.10


class Deposit:
    __slots__ = ('initial_investment', 'investment_len_in_years', 'interest_rate')

    def __init__(self,
                 initial_investment: int,
                 investment_in_years: int,
                 interest_rate: float | int = INTEREST_RATE_DEFAULT):

        if initial_investment < 0:
            raise ValueError("Initial investment cannot be negative")

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
