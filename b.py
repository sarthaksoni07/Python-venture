#sum of first n element
x = int(input("please enter the number - "))
sum = 0
for i in range(0,x+1):
    sum+=i
print(sum)
 #2
#3
isPrime=True
for i in range(2,x):
    if x%i==0:
        isPrime=False
if isPrime==True:
    print("prime")
else:
    print("non prime")

#4
y= int(input("plase enter the exponent"))
z=x**y
print(z)

#5
print(int(str(x)[::-1]))

#6
sum = 0
for i in range(0,len(x)):
    sum+=(int(str(x[i]))**len(str(x)))
if sum==int(x):
    print("armstrong")
else:
    print("not armstron")


    
