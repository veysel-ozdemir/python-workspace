# change a range of item values
mylist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
mylist[1:4] = ["grape", "pear"]
print(mylist)

# insert items
mylist = ["apple", "banana", "cherry"]
mylist.insert(1, "orange")
mylist.sort(reverse=True)
print(mylist)

# looping using list comprehension
mylist = ["apple", "banana", "cherry"]
[print(x) for x in mylist]

mytuple = ("apple", "banana", "cherry")
newtuple = ("orange",)
mytuple += newtuple
print(mytuple)

mydict = {"brand": "Ford", "model": "Mustang", "year": 1964}
for x in mydict.items():
    print(type(x))

x = lambda a, *b: a * b
print(x(5, 6))


class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self)

    def __str__(self) -> str:
        return f"{self.firstname}, {self.lastname}"


x = Person("X", "Y")
x.printname()


class Student(Person):
    pass


x = Student("T", "Z")
x.printname()


class C:
    counter = 0

    def __init__(self):
        C.counter += 1  # type(self).counter += 1

    def __del__(self):
        type(self).counter -= 1


x = C()
print(f"Number of instances: {C.counter}")
y = C()
print(f"Number of instances: {C.counter}")
del x
print(f"Number of instances: {C.counter}")
del y
print(f"Number of instances: {C.counter}")


class P:
    def __init__(self, val):
        self.xset = val

    @property
    def xget(self):
        return self.__x

    @xget.setter
    def xset(self, n):
        if n < 0:
            self.__x = 0
        elif n > 1000:
            self.__x = 1000
        else:
            self.__x = n


p = P(1001)
print(p.xget)
p.xset = 1001
print(p.xget)


def decorator(*args, **kwargs):
    print("Inside decorator")

    def inner(func):
        print("Inside inner function")
        print("I like", kwargs["like"])
        func()

    return inner


@decorator(like="Python")
def my_func():
    print("Inside actual function")


def decorator_func(x, y):
    def inner(func):
        def wrapper(*args, **kwargs):
            print("I like Python")
            print("Summation of values:" + str(x + y))
            func(*args, **kwargs)

        return wrapper

    return inner


def my_fun(*args):
    for arg in args:
        print(arg)


decorator_func(10, 25)(my_fun)("Hello", "my", "Python")
