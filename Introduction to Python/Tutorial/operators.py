print(24 / 5)  # result is decimal
print(24 // 5)  # rounding down (floor)
print(round(24 / 5))  # rounding up

print(2**3)  # exponential operation (2^3)

number = 10
number += 2
number -= 6
number *= 3
number /= 2  # result is decimal
print(number)

index = 0
index += 1  # index++ isn't allowed

# ------ COMPARISON OPERATORS ------
print(10 < 21)
print(10 <= 10)
print(10 > 8)
print(10 >= 10)
print(0 == 0)

# -------- BOOLEAN OPERATORS --------
x = True
y = False
z = True
print(not x)  # False
print(x and y)  # False
print(x and not y)  # True
print(x or y)  # True
print(y or not z)  # False
print(z is x)  # True
print(y is not x)  # True

# --------- TERNARY OPERATOR ---------
meaning = 12

# if meaning > 10:
#     print("Right on!")
# else:
#     print("Not today")

print("Right on!") if meaning > 10 else print("Not today")