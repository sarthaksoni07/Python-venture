class InvalidMarksError(Exception):
    pass
try:
    x = int(input("Please enter marks - "))
    if x<0 or x>100:
        raise InvalidMarksError("Marks out of range")
except InvalidMarksError as e:
    print(e)
else:
    print("marks accepted")