from home_work.hw_11.bank_deposit.deposit import Deposit, calc_end_balance

my_deposit = Deposit(initial_investment=100_000, investment_in_years=5)

print(f"Ending balance | ${calc_end_balance(my_deposit)}")
