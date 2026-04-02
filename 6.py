try :
    x = int(input("enter number 1 - "))
    y = input("enter number 2 - ") #guaranteed to fail and throw a type error
    z= x/y
except TypeError:
    print("please enter an integer value")
else:
    print(z)
