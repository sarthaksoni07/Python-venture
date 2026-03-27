print("hello world")


li = [1,3,4,5]# this is a list 
print(li[:-1])# can experiment with this with regard to the list and it's slicing features .
t = (1,2,3)# index, but not mutable ,repitions is allows in tuple , but not sets. 
#t[0]= 1 #wil throw an error. 
t2=(4,5)
a, b = t2
t3 = t+t2
print(t3, a, b)


set = {1,2,3}# not order, no repition allowed and mutable
set1 = {3,4,5}
print(set|set1)
print(set&set1)
print(set- set1)


{"sarthak" : {
    "age":21,
    "gender":"male"
}}
#dictionary , it has 3 main methods  - .item(), .values(), .keys()
