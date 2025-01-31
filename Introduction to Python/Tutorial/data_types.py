import math

# ---------------------- String data type --------------------------

# literal assignment
first = "Dave"
last = "Gray"
print(type(first))
print(type(first) == str)
print(isinstance(first, str))

# constructor function
pizza = str("Pepperoni")

# Concatenation
fullname = first + " " + last
print(fullname)

fullname += "!"
print(fullname)

# Casting a number to a string
decade = str(1980)
print(type(decade))

statement = "I like rock music from the " + decade + "s."
print(statement)

# Multiple lines
multiline = """
Hey, how are you?

I was just checking in.
                        All good?
"""
print(multiline)

# Escaping special characters
sentence = "I'm back at work!\tHey!\n\nWhere's this at\\located?"
print(sentence)

# String methods
print(first)
print(first.lower())
print(first.upper())
print(multiline)
print(multiline.title())
print(multiline.replace("good", "ok"))

print(len(multiline))
multiline += "                "
multiline = "             " + multiline
print(len(multiline))
print(len(multiline.strip()))
print(len(multiline.lstrip()))
print(len(multiline.rstrip()))

# Build a menu
title = "menu".upper()
print(title.center(20, "="))  # ========MENU========
print("Coffee".ljust(16, ".") + "$1".rjust(4, "."))  # Coffee............$1
print("Muffin".ljust(16, ".") + "$2.5".rjust(4, "."))  # Muffin..........$2.5
print("Cheesecake".ljust(16, ".") + "$4".rjust(4, "."))  # Cheesecake........$4

# String index values
print(first[0])  # first letter
print(first[-1])  # last letter
print(first[1:-1])  # inclusive index : exclusive index
print(first[0:])

# Some methods return boolean data
print(first.startswith("D"))
print(first.endswith("Z"))

# ---------------------- Boolean data type ----------------------------
myvalue = True
x = bool(False)
print(type(x))
print(isinstance(myvalue, bool))

# ---------------------- Numeric data type ----------------------------
# integer type
price = 100
best_price = int(80)
print(type(price))
print(isinstance(best_price, int))

# float type
gpa = 3.18
y = float(1.14)
print(type(gpa))
print(isinstance(y, float))

# complex type
comp_value = 5 + 3j
print(type(comp_value))
print(comp_value.real)  # 5.0
print(comp_value.imag)  # 3.0
print(comp_value.conjugate())  # (5-3j)

# Built-in functions for numbers
num = -2.93
print(abs(num))  # 2.93
print(abs(num * -1))  # 2.93
print(round(num))  # -3
print(round(num, 1))  # -2.9

print(math.pi)
print(math.sqrt(64))
print(math.ceil(gpa))  # 3.18 -> 4
print(math.floor(gpa))  # 3.18 -> 3

# Casting a string to a number
zipcode = "10001"
zip_value = int(zipcode)
print(type(zip_value))

# Error if you attempt to cast incorrect data
# zip_value = int("New York")
