# creating a comment
# print("Hello, World!")
print("Hello, Moon!")

# multiline comments
"""
This is a comment
written in
more than just one line
"""
print("Hello, World!")

# list
mylist = ["apple", "banana", "cherry"]

# allow duplicates
mylist = ["apple", "banana", "cherry", "apple", "cherry"]

# access items
mylist = ["apple", "banana", "cherry"]
print(mylist[1])

# negative indexing
mylist = ["apple", "banana", "cherry"]
print(mylist[-1])

# range of indexes (:)
mylist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(mylist[2:5])

mylist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(mylist[:2])

mylist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(mylist[4:])

# range of negative indexes
mylist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(mylist[-3:-1])

# change item value
mylist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
mylist[1] = "grape"
print(mylist)

# change a range of item values
mylist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
mylist[1:3] = ["grape", "pear"]
print(mylist)

# append items
mylist = ["apple", "banana", "cherry"]
mylist.append("orange")
print(mylist)

# insert items
mylist = ["apple", "banana", "cherry"]
mylist.insert(1, "orange")
print(mylist)

# extend list
mylist = ["apple", "banana", "cherry"]
addlist = ["mango", "pineapple", "papaya"]
mylist.extend(addlist)
print(mylist)

# remove specified item
mylist = ["apple", "banana", "cherry"]
mylist.remove("banana")
print(mylist)

# remove specified index
mylist = ["apple", "banana", "cherry"]
mylist.pop(1)
print(mylist)

mylist = ["apple", "banana", "cherry"]
mylist.pop()  # last item
print(mylist)

mylist = ["apple", "banana", "cherry"]
del mylist[0]
print(mylist)

# clear the list
mylist = ["apple", "banana", "cherry"]
mylist.clear()
print(mylist)

# loop through a list
mylist = ["apple", "banana", "cherry"]
for x in mylist:
    print(x)

# loop through the index numbers
mylist = ["apple", "banana", "cherry"]
for i in range(len(mylist)):
    print(mylist[i])

# looping using list comprehension
mylist = ["apple", "banana", "cherry"]
[print(x) for x in mylist]

# condition
mylist = ["apple", "banana", "cherry"]
newlist = [x for x in mylist if x != "apple"]
print(newlist)

# sort list alphanumerically
mylist = ["banana", "apple", "cherry"]
mylist.sort()
print(mylist)

# sort descending
mylist = ["banana", "apple", "cherry"]
mylist.sort(reverse=True)
print(mylist)

# copy a list
mylist = ["banana", "apple", "cherry"]
newlist = mylist.copy()
print(mylist)

# join two lists
mylist1 = ["apple", "banana", "cherry"]
mylist2 = ["mango", "pineapple", "papaya"]
newlist = mylist1 + mylist2
print(newlist)

# tuple
mytuple = ("apple", "banana", "cherry")
print(mytuple)

# items can be any data type
tuple1 = ("apple", 34, True, 40.3)

# access tuple items
mytuple = ("apple", "banana", "cherry")
print(mytuple[1])

# negative indexing
mytuple = ("apple", "banana", "cherry")
print(mytuple[-1])

# range of indexes
mytuple = ("apple", "banana", "cherry", "orange")
print(mytuple[1:3])

mytuple = ("apple", "banana", "cherry", "orange")
print(mytuple[:2])

mytuple = ("apple", "banana", "cherry", "orange")
print(mytuple[1:])

# range of negative indexes
mytuple = ("apple", "banana", "cherry", "orange")
print(mytuple[-3:-1])

# change tuple values
mytuple = ("apple", "banana", "cherry")
newtuple = list(mytuple)
newtuple[1] = "orange"
mytuple = tuple(newtuple)
print(mytuple)

# add items
mytuple = ("apple", "banana", "cherry")
newtuple = list(mytuple)
newtuple.append("orange")
mytuple = tuple(newtuple)
print(mytuple)

mytuple = ("apple", "banana", "cherry")
newtuple = ("orange",)
mytuple += newtuple
print(mytuple)

# remove items
mytuple = ("apple", "banana", "cherry")
newtuple = list(mytuple)
newtuple.remove("cherry")
mytuple = tuple(newtuple)
print(mytuple)

# unpacking a tuple
mytuple = ("apple", "banana", "cherry")
(green, yellow, red) = mytuple
print(green)
print(yellow)
print(red)

# loop through a tuple
mytuple = ("apple", "banana", "cherry")
for x in mytuple:
    print(x)

# loop through the index numbers
mytuple = ("apple", "banana", "cherry")
for x in range(len(mytuple)):
    print(mytuple[x])

# join two tuples
mytuple1 = ("apple", "banana", "cherry")
mytuple2 = ("mango", "pineapple", "papaya")
newtuple = mytuple1 + mytuple2
print(newtuple)

# multiply tuples
mytuple = ("apple", "banana", "cherry")
newtuple = mytuple * 2
print(newtuple)

# dictionary
mydict = {"brand": "Ford", "model": "Mustang", "year": 1964}
print(mydict)

# dictionary items
mydict = {"brand": "Ford", "model": "Mustang", "year": 1964}
print(mydict["brand"])

# dictionary items can be any data type
mydict = {
    "brand": "Ford",
    "electric": False,
    "year": 1964,
    "colors": ["red", "white", "blue"],
}

# get keys
mydict = {"brand": "Ford", "model": "Mustang", "year": 1964}
x = mydict.keys()
print(x)

# change values
mydict = {"brand": "Ford", "model": "Mustang", "year": 1964}
mydict["year"] = 2018

# adding items
mydict = {"brand": "Ford", "model": "Mustang", "year": 1964}
mydict["color"] = "red"

# removing items
mydict = {"brand": "Ford", "model": "Mustang", "year": 1964}
mydict.pop("model")
print(mydict)

mydict = {"brand": "Ford", "model": "Mustang", "year": 1964}
del mydict["model"]

# loop through a dictionary
mydict = {"brand": "Ford", "model": "Mustang", "year": 1964}
for x in mydict:
    print(x)

mydict = {"brand": "Ford", "model": "Mustang", "year": 1964}
for x in mydict.keys():
    print(x)

# loop through a dictionary
mydict = {"brand": "Ford", "model": "Mustang", "year": 1964}
for x in mydict:
    print(mydict[x])

mydict = {"brand": "Ford", "model": "Mustang", "year": 1964}
for x in mydict.values():
    print(x)

mydict = {"brand": "Ford", "model": "Mustang", "year": 1964}
for x, y in mydict.items():
    print(x, y)

# copy a dictionary
# dict2 = dict1 => dict2 will only be a reference to dict1
# and changes made in dict1 will automatically also be made in dict2.
mydict = {"brand": "Ford", "model": "Mustang", "year": 1964}
newdict = mydict.copy()
print(newdict)

# condition: if ... else
a = 10
b = 20
if b > a:
    print("b is greater than a")
else:
    print("a is greater than b")

# elif
a = 10
b = 10
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")

# short hand if
if a > b:
    print("a is greater than b")

# short hand if ... else
a = 10
b = 20
print("a") if a > b else print("b")

# loops
# while
i = 1
while i < 6:
    print(i)
    i += 1
print("\n")

# break statement
i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1
print("\n")

# continue
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)
print("\n")

# else statement
i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i is no longer less than 6")
print("\n")

# for
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
print("\n")

# break statement
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
    if x == "banana":
        break
print("\n")

# continue statement
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        continue
    print(x)
print("\n")

# range() function
for x in range(10):
    print(x)
print("\n")

for x in range(5, 10):
    print(x)
print("\n")

for x in range(1, 10, 3):
    print(x)
print("\n")


# functions
# creating a function
def my_function():
    print("Hello from a function")


# argumnets
def my_function(name):
    print("Hello, " + name)


# arbitrary arguments, *args
# the function will receive a tuple of arguments, and can access the items accordingly
def my_function(*names):
    print("First name is " + names[0])


# arbitrary keyword arguments, **kwargs
# pretends the passed argument as a dictionary
def my_function(**person):
    print("Last name is " + person["lastname"])


my_function(firstname="X", lastname="Y")


# default parameter value
def my_function(country="Norway"):
    print("I am from " + country)


my_function()
my_function("Brazil")


# passing a data type as an argument
def my_function(food):
    for x in food:
        print(x)


fruits = ["apple", "banana", "cherry"]
my_function(fruits)


# return values
def my_function(x):
    return 5 * x


print(my_function(4))


# pass statement
def myfunction():
    pass


# lambda funtion
# A lambda function is a small anonymous function. A lambda function can take any number of arguments, but can only have one expression.
x = lambda a: a + 10
print(x(5))
x = lambda a, b: a * b
print(x(5, 6))


# classes and objects
# create a class
class MyClass:
    x = 5


# create object
p1 = MyClass()
print(p1.x)


# The __init__() Function
# The examples above are classes and objects in their simplest form, and are not really useful in real life
# applications. To understand the meaning of classes we have to understand the built-in __init__() function.
# All classes have a function called __init__(), which is always executed when the class is being initiated.
# Use the __init__() function to assign values to object properties, or other operations that are necessary to
# do when the object is being created.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


p1 = Person("X", 36)
print(p1.name)
print(p1.age)


# The __str__() Function
# The __str__() function controls what should be returned when the class object is represented as a string.
# If the __str__() function is not set, the string representation of the object is returned:
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}({self.age})"


p1 = Person("John", 36)
print(p1)


# object methods
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my name is " + self.name)


p1 = Person("John", 36)
p1.myfunc()

# modify object properties
p1.age = 40

# delete object properties
del p1.age


# create a parent class
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)


x = Person("X", "Y")
x.printname()


class Student(Person):
    pass


x = Student("T", "Z")
x.printname()


# scope
# local scope
def myfunc():
    x = 300
    print(x)


myfunc()


# function inside funtion
def myfunc():
    x = 300

    def myinnerfunc():
        print(x)

    myinnerfunc()


myfunc()

# global scope
x = 300


def myfunc():
    print(x)


myfunc()
print(x)

# naming variables
x = 300


def myfunc():
    x = 200
    print(x)


myfunc()
print(x)
