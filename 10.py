class WeakPasswordError(Exception):
    pass
try:
    x = input("Please Enter Your password")
    if len(x)<8:
        raise WeakPasswordError("Password lenght insufficient")
    if any(char.isdigit() for char in x):
        raise WeakPasswordError("Digit found")

except WeakPasswordError as e:
    print(e)
else:
    print("password accepted")
