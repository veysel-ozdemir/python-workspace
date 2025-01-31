def fact(num):
    if num <= 1:
        return 1
    else:
        return num * fact(num - 1)


print(fact(5))


def add_one(num):
    if num >= 9:
        return num + 1
    total = num + 1
    print(total)
    return add_one(total)


add_one(0)  # output will be 1 to 9
print(add_one(0))  # output will be 1 to 10
