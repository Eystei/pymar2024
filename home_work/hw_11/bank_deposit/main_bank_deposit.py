from home_work.hw_11.bank_deposit.bank import Bank

C_ID = "0000001"
C_NAME = "Pikachu"

bank = Bank()
bank.register_client(client_id=C_ID, name=C_NAME)
bank.open_deposit_account(client_id=C_ID, start_balance=1000, years=5)
print(f"Check final balance : {bank.calc_interest_rate(client_id=C_ID)}")
bank.close_deposit(client_id=C_ID)

bank.exchange_currency(from_curr='eur', amount=1000, to_curr='pln')
