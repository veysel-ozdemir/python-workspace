nums = {1, 2, 3, 4}
nums2 = set((1, 2, 3, 4))

print(nums)
print(nums2)
print(type(nums))
print(len(nums))

## you cannot refer to an element in the set with an index position or a key

## no duplicates allowed
nums = {1, 2, 2, 3}
print(nums)  # ignores the duplicates

## True is a dupe of 1, False is a dupe of zero
nums = {1, True, 2, False, 3, 4, 0}
# '1' and 'False' will appear first. Therefore, they will be printed.
print(nums)  # {False, 1, 2, 3, 4}

## check value
print(2 in nums)

## add a new element to a set
nums.add(8)
print(nums)

## add elements from one set to another
morenums = {5, 6, 7}
nums.update(morenums)
print(nums)

## merge two sets to create a new set
one = {1, 2, 3}
two = {5, 6, 7}
newset = one.union(two)
print(newset)  # {1, 2, 3, 5, 6, 7}

## keep only the duplicates
one = {1, 2, 3}
two = {2, 3, 4}
one.intersection_update(two)
print(one)  # {2, 3}

## keep everything except the duplicates
one = {1, 2, 3}
two = {2, 3, 4}
one.symmetric_difference_update(two)
print(one)  # {1, 4}
