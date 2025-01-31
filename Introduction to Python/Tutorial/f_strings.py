person = "Karl"
coins = 3

# older way
print("\n%s has %s coins left." % (person, coins))

# with concatenation
print("\n" + person + " has " + str(coins) + " coins left.")

# the format methods
print("\n{} has {} coins left.".format(person, coins))  # positional
print("\n{1} has {0} coins left.".format(coins, person))  # indexing
print("\n{person} has {coins} coins left.".format(coins=coins, person=person))  # named

player = {
    "person": "Karl",
    "coins": 3,
}
print("\n{person} has {coins} coins left.".format(**player))  # with dictionary

# best approach: f-Strings
print(f"\n{person} has {coins} coins left.")
print(f"\n{person} has {2 * 5} coins left.")
print(f"\n{person.lower()} has {2 * 5} coins left.")
print(f"\n{player['person'].upper()} has {player['coins'] * 3} coins left.")

# pass formatting options
num = 10
print(f"\n2.25 times {num} is {2.25 * num:.3f}\n")  # f stands for 'fixed'
# .3 describes the number of digit for the decimal part

for num in range(1, 11):
    print(f"2.25 times {num} is {2.25 * num:.3f}")

for num in range(1, 11):
    print(f"{num} divided by 4.52 is {num / 4.52:.2%}")  # % stands for percentage
