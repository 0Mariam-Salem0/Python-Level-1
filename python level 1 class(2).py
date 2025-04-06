#Start of 2 meetings (3 and 4)
#Lecture 3
#Slicing
#start index and the end index (from the start to the number before the last number)
#[ : ]
a = "Hello, World!"
print(a[0:12])
print(a[0:13])
print(a[0:5])
print(a[1:5])
print(a[1:6])
print(a[2:12])
print(a[3:9])
print("----------------------------------------")
#Slice from the start
b = "Hello, World!"
print(b[:5])
print(b[:3])
print("----------------------------------------")
#Slice to the end
print(b[5:])
print(b[3:])
print("----------------------------------------")
#Negative indexing
#[- :- ]
c = "Hello, World!"
print(c[-5:-2])
print(c[-2:-1])
print("----------------------------------------")
#Modify strings
#Upper case
#upper()
a = "Hello, World!"
print(a.upper())
#Lower case
#lower()
b = "Hello, World!"
print(b.lower())
print("----------------------------------------")
#Remove whitespace
#split()
a = " Hello, World! "
print(a)
print(a.strip())
print("----------------------------------------")
#Replace string
#replace()
b = "Hello, World!"
print(b.replace("l", "p"))
print("----------------------------------------")
#Split string
#split()
c = "Hello & World!"
print(c.split('&'))
print(c.split('e'))
print("----------------------------------------")
#String concatenation
#we use + operator
a = "Hello"
b = "World"
c = a + b
print(c)
print("----------------------------------------")
x = "Hello"
y = "World"
z = x + " " + y
print(z)
print("----------------------------------------")
#String methods
#String format
#format()
age = 22
txt = "My name is John, I am " + str(age)
print(txt)
#txt = "My name is John, I am " + age
#print(txt)
#TypeError: can only concatenate str (not "int") to str
print("----------------------------------------")
age = 22
txt = "My name is John and I am {}"
print(txt.format(age))
print("----------------------------------------")
quantity = 4
item_no = 789
price = 55.78
my_order = "I want {} pieces of item {} for {} LE"
print(my_order.format(quantity, item_no, price))
print("----------------------------------------")
#capitalize()
a = "hello world"
print(a.capitalize())
print("----------------------------------------")
#casefold()
b = "HeLLo World"
print(b.casefold())
print("----------------------------------------")
#count()
c = "hello world"
print(c.count("l"))
print("----------------------------------------")
#endswith()
d = "hello world"
print(d.endswith("hello"))
print(d.endswith("world"))
print("----------------------------------------")
#find()
e = "hello world"
print(e.find("l"))
print("----------------------------------------")
#index()
f = "hello world"
print(f.index("o"))
print("----------------------------------------")
#isalpha()
g = "hello_world"
print(g.isalpha())
h = "helloworld"
print(h.isalpha())
print("----------------------------------------")
#isdigit()
i = "helloworld"
print(i.isdigit())
j = "123456789"
print(j.isdigit())
print("----------------------------------------")
#islower()
k = "HeLLo World"
print(k.islower())
l = "hello world"
print(l.islower())
print("----------------------------------------")
#Python conditions & if statement
s = """Equals: a == b
Not equals: a != b
Less than: a < b
Less than or equal to: a <= b
Greater than: a >= b
Greater than or equal to: a >= b
"""
print(s)
print("----------------------------------------")
#If
a = 22
b = 222
if b > a:
    print("b is greater than a")
#if b > a:
#print("b is greater than a")
#IndentationError: expected an indented block after 'if' statement
print("----------------------------------------")
#Elif
a = 22
b = 22
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
print("----------------------------------------")
#Else
a = 200
b = 22
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
    print("a is greater than b")
print("----------------------------------------")
print("1 = +")
print("2 = -")
print("3 = *")
print("4 = /")
operator = input("please choose a number from 1 to 4:\n")
first_num = input("please insert the first number:\n")
second_num = input("please insert the second number:\n")
print("The answer is:")
if int(operator) == 1:
    print(int(first_num) + int(second_num))
elif int(operator) == 2:
    print(int(first_num) - int(second_num))
elif int(operator) == 3:
    print(int(first_num) * int(second_num))
elif int(operator) == 4:
    print(int(first_num) / int(second_num))
print("----------------------------------------")
#Lecture 4
#Python dictionaries
#Dictionary
#key: value
car = {
    "brand": "toyota",
    "model": "corolla",
    "year": 2016
}
print(car)
print("----------------------------------------")
#Dictionary items
car = {
    "brand": "toyota",
    "model": "corolla",
    "year": 2016
}
print(car["brand"])
print(car["model"])
print(car["year"])
print("----------------------------------------")
#Duplicates not allowed
"""
car = {
    "brand": "toyota",
    "brand": "ford",
    "model": "corolla",
    "model": "mustang",
    "year": 2016,
    "year": 2019
}
print(car)
print(car["brand"])
print(car["model"])
print(car["year"])
"""
print("----------------------------------------")
#Dictionary length
#print(len())
car = {
    "brand": "toyota",
    "model": "corolla",
    "year": 2016,
    "item": "num_1"
}
print(len(car))
print("----------------------------------------")
#Dictionary items - Data types
car = {
    "brand": "toyota",
    "model": True,
    "year": 2016,
    "item": ["red", "blue", "white"],
    "item": {"red","blue"}
}
print(car)
print("----------------------------------------")
#Python - Access dictionary items
car = {
    "brand": "toyota",
    "model": "corolla",
    "year": 2016
}
#2 ways to get the value from the variable
#name of the dictionary ["the name of the key"]
#name of the dictionary.get("the name of the key")
x = car["model"]
print(x)
print("----------------------------------------")
y = car.get("year")
print(y)
print("----------------------------------------")
#Get keys
car = {
    "brand": "toyota",
    "model": "corolla",
    "year": 2016
}
x = car.keys()
print(x)
car["color"] = "blue"
print(x)
print(car)
print("----------------------------------------")
#Get values
car = {
    "brand": "toyota",
    "model": "corolla",
    "year": 2016
}
x = car.values()
print(x)
car["year"] = 2020
print(x)
print(car)
print("----------------------------------------")
#Add values
car = {
    "brand": "toyota",
    "model": "corolla",
    "year": 2016
}
x = car.values()
print(x)
car["color"] = "red"
print(x)
print(car)
print("----------------------------------------")
#Python loops
#While loop
#statement is executed as long as the condition is true
#Starting from 0
i = 1
while i < 6:
    print(i)
    i += 1
    #Increment
print("----------------------------------------")
#Brek statement
#stop the loop even if while condition is true
i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1
print("----------------------------------------")
#Continue statement
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)
print("----------------------------------------")
#Else statement
i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i is no longer less than 6")
print("----------------------------------------")
#For loop
#statement is executed once for each item
#Iterating
fruits = ["apple", "orange", "banana"]
for i in fruits:
    print(i)
print("----------------------------------------")
#Looping through a string
for i in "banana":
    print(i)
print("----------------------------------------")
#Break statement
fruits = ["apple", "banana", "orange"]
for i in fruits:
    print(i)
    if i == "banana":
        break
print("----------------------------------------")
fruits = ["apple", "banana", "orange"]
for i in fruits:
    if i == "banana":
        break
    print(i)
print("----------------------------------------")
#Continue statement
fruits = ["apple", "banana", "orange"]
for i in fruits:
    if i == "banana":
        continue
    print(i)
print("----------------------------------------")
""" 
fruits = ["apple", "banana", "orange"]
for i in fruits:
    print(i)
    if i == "banana":
        continue
"""
print("----------------------------------------")
#Nested loops
colors = ["red", "blue", "green"]
fruits = ["apple", "banana", "orange"]
for i in colors:
    for k in fruits:
        print(i, k)
print("----------------------------------------")
cars = ["toyota", "mitsubishi", "ford"]
for l in cars:
    print(l)
print("----------------------------------------")
cars = ["toyota", "mitsubishi", "ford"]
for l in cars:
    if l == "mitsubishi":
        continue
    print(l)
print("----------------------------------------")
cars = ["toyota", "mitsubishi", "ford"]
for l in cars:
    print(l)
    if l == "toyota":
        break
print("----------------------------------------")
n = 0
while n < 100:
    n += 1
    if n % 2 == 0:
        continue
    print(n)
print("----------------------------------------")
n = -1
while n <= 100:
    n += 1
    if n % 2 != 0:
        continue
    print(n)
print("----------------------------------------")
#End of 2 meetings
