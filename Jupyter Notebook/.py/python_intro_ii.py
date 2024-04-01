# copy vs reference
a = [100]
b = a
c = a.copy()

print(id(a))
print(id(b))
print(id(c))

print(type(a))
print(type(b))
print(type(c))

# static methods


# public attribute
class C:
    counter = 0

    def __init__(self):
        type(self).counter += 1  # C.counter += 1

    def __del__(self):
        type(self).counter -= 1  # C.counter += 1


x = C()
print(f"Number of instances: {C.counter}")
y = C()
print(f"Number of instances: {C.counter}")
del x
print(f"Number of instances: {C.counter}")
del y
print(f"Number of instances: {C.counter}")


# private attribute (double underscore makes it private)
class Robot:
    __counter = 0

    def __init__(self):
        type(self).__counter += 1

    def RobotInstances(self):
        return Robot.__counter


x = Robot()
print(x.RobotInstances())
y = Robot()
print(x.RobotInstances())
# print(Robot.RobotInstances()) # error
# reference to an instance is required for calling
print(f"{Robot.RobotInstances(y)}\n")


# static methods don't need a reference to an instance
class Robot:
    __counter = 0

    def __init__(self):
        type(self).__counter += 1

    @staticmethod
    def RobotInstances():
        return Robot.__counter


print(Robot.RobotInstances())
x = Robot()
print(x.RobotInstances())
y = Robot()
print(x.RobotInstances())
print(Robot.RobotInstances())

# class methods
# Like static methods class methods are not bound to
# instances, but unlike static methods class methods
# are bound to a class. The first parameter of a
# class method is a reference to a class,
# i.e. a class object. They can be called via an
# instance or the class name


class Robot:
    __counter = 0

    def __init__(self):
        type(self).__counter += 1

    @classmethod
    def RobotInstances(cls):
        return cls, Robot.__counter


print(Robot.RobotInstances())
x = Robot()
print(x.RobotInstances())
y = Robot()
print(x.RobotInstances())
print(Robot.RobotInstances())

# greatest common divisor (gcd)
# the greatest common divisor of two or more integers,
# is the largest positive integer that divides the numbers
# without a remainder


class fraction:
    def __init__(self, n, d):
        self.numerator, self.denominator = fraction.reduce(n, d)

    @staticmethod
    def gcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a

    @classmethod
    def reduce(cls, n1, n2):
        g = cls.gcd(n1, n2)
        return (n1 // g, n2 // g)

    def __str__(self):
        return f"{self.numerator} / {self.denominator}"


x = fraction(8, 24)
print(x)

# properties
# A method which is used for getting a value is
# decorated with @property, i.e. we put this line
# directly in front of the header. The method which
# has to function as the setter is decorated with
# @x.setter. If the function had been called f, we
# would have to decorate it with @f.setter.


class P:
    def __init__(self, x):
        self.x = x

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if x < 0:
            self.__x = 0
        elif x > 1000:
            self.__x = 1000
        else:
            self.__x = x


p1 = P(1001)
print(p1.x)
p1.x = 1001
print(p1.x)

# class P:
#     def __init__(self, val):
#         self.xset = val
#     @property
#     def xget(self):
#         return self.__x
#     @xget.setter
#     def xset(self, n):
#         if n < 0:
#             self.__x = 0
#         elif n > 1000:
#             self.__x = 1000
#         else:
#             self.__x = n

# p = P(1001)
# print(p.xget) # 1000
# p.xset = 1001
# print(p.xget) # 1000

print("\n")


class P:
    def __init__(self, x):
        self.set_x(x)

    def get_x(self):
        return self.__x

    def set_x(self, x):
        if x < 0:
            self.__x = 0
        elif x > 1000:
            self.__x = 1000
        else:
            self.__x = x


p1 = P(1001)
print(p1.get_x())
p1.set_x(1001)
print(p1.get_x())
p1.x = 1001  # !
print(p1.x)

# exceptions

# try-except block
try:
    a = 10
    b = 0
    c = a / b
    print(f"{a}/{b} = %d" % c)
except:
    print("Can't divide with zero. Provide different number.")

print("\n")

# multiple except blocks
try:
    a = int(input("Enter value of a: "))
    b = int(input("Enter value of b: "))
    c = a / b
    print(f"{a}/{b} = %d" % c)
except ValueError:
    print("Entered value is wrong.")
except ZeroDivisionError:
    print("Can't divide by zero.")
# combine both exceptions
# except (ValueError, ZeroDivisionError):
#     print("Please enter a valid value.")

print("\n")

# finally block
# The finally block is used to write a block of code
# that must execute, whether the try block raises an
# error or not.
try:
    a = int(input("Enter value of a: "))
    b = int(input("Enter value of b: "))
    c = a / b
    print(f"{a}/{b} = %d" % c)
except (ValueError, ZeroDivisionError):
    print("Please enter a valid value.")
finally:
    print("Inside the finally block.")

print("\n")

# else block
# The else block will be executed if and only if
# there are no exception occured in the try block.
# The else block can be used with the finally block.
try:
    a = int(input("Enter value of a: "))
    b = int(input("Enter value of b: "))
    c = a / b
    print(f"{a}/{b} = %d" % c)
except (ValueError, ZeroDivisionError):
    print("Please enter a valid value.")
else:
    print("No error occured.")
finally:
    print("All finished.")


print("\n")


# raising an exception
def simple_interest(amount, year, rate):
    try:
        if rate > 100:
            raise ValueError(rate)
        interest = (amount * year * rate) / 100
        print("The Simple Interest is", interest)
        return interest
    except ValueError:
        print("Interest rate is out of range", rate)


print("Case 1")
simple_interest(800, 6, 8)
print("Case 2")
simple_interest(800, 6, 800)


# *args and **kwargs
# *args receives arguments as a tuple.
def myFunction(*arguments):
    for arg in arguments:
        print(arg)


myFunction("Hello", "Welcome", 2, "Python!")

print("\n")


def myFunction(arg1, *arguments):  # the arg1 has to be positioned firstly
    print("First argument:", arg1)
    for arg in arguments:
        print("Next argument through:", arg)


myFunction("Hello", "Welcome", 2, "Python!")

print("\n")


# **kwargs reveives arguments as a dictionary
def myFunction(**kwargs):
    print(kwargs)
    for key, value in kwargs.items():
        print("%s : %s" % (key, value))


myFunction(name="Alex", lastname="Paul", year=2001)

print("\n")


# passing *args and **kwargs to a function as arguments
# The length of *args and the item count of **kwargs,
# must be equal to the parameter count of function.
def myFunction(arg1, arg2, arg3):
    print("arg1:", arg1)
    print("arg2:", arg2)
    print("arg3:", arg3)


args = ("Welcome", "to", "Python")
myFunction(*args)

# the keys of dictionary have to be defined
# same as the parameters of the function
kwargs = {"arg1": "Welcome", "arg2": "to", "arg3": "Python"}
myFunction(**kwargs)

print("\n")


# using both
def myFunction(*args, **kwargs):
    print("args:", args)
    print("kwargs:", kwargs)


myFunction("Hello", "to", "Python", first="Hallo", mid="zu", last="Python")
# ! Positional argument cannot appear after keyword arguments
# myFunction(first = 'Hallo', mid = 'zu', 'Hello', 'to', 'Python') # error

print("\n")


class car:
    def __init__(self, *args):
        self.speed = args[0]
        self.color = args[1]


audi = car(200, "red")
bmw = car(250, "black")
print(audi.color)
print(bmw.speed)

print("\n")


class car:
    def __init__(self, **kwargs):
        self.speed = kwargs["s"]
        self.color = kwargs["c"]


audi = car(s=200, c="red")
bmw = car(s=250, c="black")
print(audi.color)
print(bmw.speed)

# decorator
# The decorators allow us to wrap another function
# in order to extend the behaviour of the wrapped
# function, without permanently modifying it.

# first class objects
# Functions are first class objects which means that functions
# in Python can be used or passed as arguments.
# Properties of first class functions:
# - A function is an instance of the Object type.
# - You can store the function in a variable.
# - You can pass the function as a parameter to another function.
# - You can return the function from a function.
# - You can store them in data strucures such as hash tables, lists, ...


# functions can be treated as objects
def message(text):
    return text.upper()


print(message("Hello"))
newMessage = message
print(newMessage("Hola"))


# functions can be passed as arguments to other functions
def messageU(text):
    return text.upper()


def messageL(text):
    return text.lower()


def greet(func):
    greeting = func("Hello, this is test message.")
    print(greeting)


greet(messageU)
greet(messageL)


# returning functions from another function
def create_adder(x):
    def adder(y):
        return x + y

    return adder


add_15 = create_adder(15)
print(add_15(10))


def increase(x):
    return x + 1


def decrease(x):
    return x - 1


def operation(func, x):
    result = func(x)
    return result


print(operation(increase, 4))
print(operation(decrease, 4))


def calling():
    def returned():
        print("Hello")

    return returned


new = calling()
new()


# decorator expands function
# using @ to determine decorator function
# the decorator function is executed when the
# decorated function is called (not executed), i.e. divide().
def new_divide(func):
    def inner(a, b):
        print(f"Divide: {a} and {b}")
        if b == 0:
            return "You cannot divide by 0."
        return func(a, b)

    return inner


@new_divide
def divide(a, b):
    return a / b


print(divide(10, 5))
print(divide(0, 4))
print(divide(5, 0))


def hello_decorator(func):
    def inner(*args, **kwargs):
        print("Before Execution")
        returned_value = func(*args, **kwargs)
        print("After Execution")
        return returned_value

    return inner


@hello_decorator
def sum_two_numbers(a, b):
    print("Inside the function")
    return a + b


a, b = 1, 2
print(f"Sum = {sum_two_numbers(a,b)}\n")

# examples
import time
import math


def calculate_time(func):
    def inner(*args, **kwargs):
        begin = time.time()
        func(*args, **kwargs)
        end = time.time()
        print("Total time taken in : ", func.__name__, end - begin)

    return inner


@calculate_time
def factorial(num):
    time.sleep(2)
    print(math.factorial(num))


@calculate_time
def fibonacci(num):
    n1, n2 = 0, 1
    count = 0
    print("Fibonacci sequence:")
    while count < num:
        print(
            n1,
        )
        next = n1 + n2
        n1 = n2
        n2 = next
        count += 1


factorial(10)
print(fibonacci(10))


# chaining decorator
# the decorators will be execute top-down respectively
def decor1(func):
    def inner():
        x = func()
        return x * x

    return inner


def decor2(func):
    def inner():
        x = func()
        return 2 * x

    return inner


@decor1
@decor2
def num():
    return 10


@decor2
@decor1
def num2():
    return 10


print(num())  # 400
print(num2())  # 200


# decorators with parameters
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


# super() function
class A:
    def greet(self):
        print("Hello from class A!")


class B(A):
    def greet(self):
        super().greet()  # Calling the greet() method of class A
        print("Hello from class B!")


b = B()
b.greet()


# polymorphism
class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must implement the 'area' method.")


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius


shapes = [Rectangle(5, 4), Circle(3)]
for shape in shapes:
    print(shape.area())

# abstract method
from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

    def calculate_area(shape):
        if isinstance(shape, Shape):
            return shape.area()
        else:
            raise TypeError("Expected an object of type Shape.")


a = Rectangle(10, 20)
print(Rectangle.calculate_area(a))
