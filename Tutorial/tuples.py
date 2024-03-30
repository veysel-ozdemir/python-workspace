mytuple = tuple(("Dave", 42, True))
anothertuple = (1, 4, 2, 8, 2, 2)

# -------------- type --------------

print(mytuple)
print(type(mytuple))
print(type(anothertuple))

# -------------- modifying --------------

newlist = list(mytuple)
newlist.append("Neil")  # type: ignore
newtuple = tuple(newlist)
print(newtuple)

# -------------- methods --------------

(one, two, *three) = anothertuple
print(one)
print(two)
print(three)  # returns remain values as a list

print(anothertuple.count(2))  # counts how many '2's are in the tuple
print(
    anothertuple.index(2)
)  # returns the index of the first appearance of '2' in the tuple
