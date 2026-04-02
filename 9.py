class InsufficientBalanceError(Exception):
    pass
balance=100
try:
    x = int(input("please enter withdrawal balance"))
    if x>balance:
        raise InsufficientBalanceError("amount is more than balance")
except InsufficientBalanceError as e:
    print(e)
else:
    balance-=x
    print(f"remaining balance {balance}")
