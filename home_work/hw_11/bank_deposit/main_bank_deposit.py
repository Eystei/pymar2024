from home_work.hw_11.bank_deposit.bank import Bank

c_id = "0000001"
c_name = "Pikachu"

bank = Bank()
bank.register_client(client_id=c_id, name=c_name)
bank.open_deposit_account(client_id=c_id, start_balance=1000, years=5)
print(f"Check final balance : {bank.calc_interest_rate(client_id=c_id)}")
bank.close_deposit(client_id=c_id)
