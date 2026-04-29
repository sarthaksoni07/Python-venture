# practice programs 
s = "sarthak"
count1=0
for i in s:
    count1+=1
print(count1)

# 2
print(s[::-1])

#3
if s==s[::-1]:
    print("pallindrome")
else:
    print("not pallindrome")

#4
a = "I am the one"
b = a.split(" ")
print(len(b))


#5
stri = "sunshine"
print("s"+stri[1::].replace("s","#"))


# #6
# b = input("please enter the string to replace")
# if b.endswith("ing"):
#     print(b+"ly")

# else:
#     print(b+"ing")

#7
print(s[::2])
print(s[::-2])

#8 
for i in range(0,len(s)):
    print(s[i])

#9 
if "sar" in s: #membership operator means I, not substr method\
    print("pos")
else:
    print("neg")

# 10 
d = input("please enter string to find() and index()")
e = input("please enter the string to find , and get it's index")
print(d.find(e))# return -1 if not found, is only for string 
print(d.index(e))# returns Value error if not found, is also for list, tuples etc
#11
print(d.count(e)) #returns number of occurences 
#12
#13
#14
print(s.replace("sarthak","sparsh"))
if s.endswith("k"):
    print(s+" soni")
else:
    print(" sparsh")

print("-".join(a.split()))
