y = 10
try :
    x = int(input("Please enter the number - "))
    z = y/x
except ZeroDivisionError:
    print("number not divisible")
except ValueError:
    print("wrong data type")
else :
    print(z)
finally:
    print("operation completed")