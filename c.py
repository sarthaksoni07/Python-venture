
#pattern printing

for i in range(1,5):
    print(" "*(5-i), end="")
    for j in range(i,0, -1):
        print(j, end="")
    for j in range(2, i+1):
        print(j,end="")
    print()

#     1
#    212
#   32123
#  4321234



x= input("please enter the string")
# y= input("please enter the charater to be replaced")
# print("".join(x.split(y)))# input java output jv
index=0
for i in x:
    if i=="n":
        x=x[:index+1]+"e"+x[index+3:]
    index+=1
print(x)
