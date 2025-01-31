# function without parameters
def hello_world():
    print("Hello world!")


hello_world()


# parameters with default values
def sum(num1=0, num2=0):
    if type(num1) is not int or type(num2) is not int:
        return 0
    return num1 + num2


total = sum(7, 2)
print(total)


# unknown number of arguments (specifying by *)
def multiple_items(*args):
    print(args)
    print(type(args))  # the type is tuple


multiple_items("Dave", "John", "Sara")
multiple_items(["Dave", "John", "Sara"])
multiple_items({1, 2, 3, 1})
multiple_items({1: "1", 2: "2", 3: "3"})


# keyword arguments: passing values by assigning them to self-defined keys.
def mult_named_items(**kwargs):
    print(kwargs)
    print(type(kwargs))  # the type is dictionary


names = ["Sam", "Samantha", "Carl", "Carlito"]
mult_named_items(first=names[0], mid=names[1], last=names[-1])
