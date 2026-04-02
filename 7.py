class NegaiveNumberError(Exception):
    pass
try:
    x = int(input())
    if x<0:
        raise NegaiveNumberError()
except NegaiveNumberError:
    print("number entered is negative")
else:
    print(f"number is {x}")
