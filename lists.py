users = ["Dave", "John", "Sara"]
data = ["Dave", 42, True]
emptylist = []

# -------------------- find item or index --------------------

print("Dave" in emptylist)
print(users.index("Sara"))

print(users[0:2])  # 2 is exclusive
print(users[1:])

# ------- append, insert, replace, and delete item or list -------

print(len(data))

users.append("Elsa")
print(users)

users += ["Jason", "Cylne"]
print(users)

users.extend(["Cris", "Cristina"])
print(users)
# users.extend(data)
# print(users)

users.insert(0, "Bob")
print(users)

users[2:2] = ["Eddie", "Alex"]  # not replacing but inserting
print(users)

users[1:3] = ["Robert", "JPJ"]  # replacing
print(users)

users.remove("Bob")
print(users)

print(users.pop())  # return the last item and remove it
print(users)

del users[0]
print(users)

# del data
# print(data) # error ocurred
data.clear()
print(data)

# -------------------- sort, reverse list --------------------

users[1:2] = ["dave"]  # replacing
users.sort()  # alphabetic order (lowercases will come all after the uppercases)
print(users)

users.sort(key=str.lower)  # include the lowercases in the alphabetic order
print(users)

nums = [4, 42, 78, 1, 5]
nums.reverse()  # not ordering!
print(nums)

# nums.sort(reverse=True)  # sort in descending order
# print(nums)

print(sorted(nums, reverse=True))
print(nums)  # not modified

# -------------------- copy and reference --------------------

ref = nums  # creating a reference
# creating copy in 3 ways
copy1 = nums.copy()
copy2 = list(nums)
copy3 = nums[:]

# -------------------- type of list --------------------

print(type(nums))

mylist = list([1, "Neil", False])
print(mylist)
