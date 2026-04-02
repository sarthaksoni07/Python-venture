list= [1,2,3,4,5]
try:
    for i in range(0,7):
        print(list[i])
except IndexError:
    print("Index out of bound error")
else:
    print("code executed")
