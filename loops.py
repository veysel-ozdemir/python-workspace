value = 0
while value < 10:
    value += 1
    if value == 5:
        continue
    elif value == 7:
        print(f"breaking the loop where value is {value} now")
        break
    print(value)

# the while loop will consider 'val' as True
# the output will be '1'
val = "y"
count = 0
while val:
    count += 1
    print(count)
    if count == 5:
        break
    else:
        val = False  # x = 0
        continue

names = ["Dave", "Sara", "John"]
for name in names:
    print(name)

for letter in "Mississippi":
    print(letter)

for x in names:
    if x == "Sara":
        continue
    print(x)

for x in range(4):  # 4 is exclusive
    print(x)

for x in range(2, 4):  # 2 is inclusive, 4 is exclusive
    print(x)

for x in range(0, 100, 10):  # start (inclusive), end (exclusive), increment
    print(x)

actions = ["codes", "eats", "sleeps"]

for name in names:
    for action in actions:
        print(name + " " + action + ".")

for action in actions:
    for name in names:
        print(name + " " + action + ".")
