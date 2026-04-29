#list tuples set and dictionaries
li=[1,2,3,4]
li.append(5)
li.remove(1)
li2=[6,7,8]
li = li+li2
li.insert(0, 1)
li.insert(0, 2)
print(li[::-1]) #smae work as slicing in lists
print(li)
li.pop(2)
print(li)

#tuples

ti = (1,2,3)
# indexed 
print(ti[0])
ti1= (3,4,5) #cann be added
ti=ti+ti1
print(ti)
#immutable , cannot change the value
ti2 = ("sarhtak",22, "it")
name, age, dept = ti2 # this is used to fetch data from tuples
print(name,age,dept)


di = {
    "name":"Sarthak",
    "sname":"soni"
}
print(di.items())
print(di.values())
print(di["name"])
di1= {
    "names":["sarthak", "sparsh", "rahul"],
    "marks":[100,200,200],
    "comments":{
        "sarthak":"fine",
        "sparsh":"great",
        "rahul":"fire"
    }
}
print(di1["names"][0])
print(di1["comments"]["sparsh"])
