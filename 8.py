class InvalidAgeError(Exception):
    pass
try:
    x = int(input("Please enter your age - "))
    if x<18:
        raise InvalidAgeError("Not Eligible")
    elif x>60:     
        raise InvalidAgeError("Too old for this policy")
except InvalidAgeError as e:
    print(f"Error : {e}")
else:
    print("accepted")
