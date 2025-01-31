# closure is a function having access to the scope of its parent
# function after the parent function has returned.


def parent_funct(person, coins):
    # coins = 3

    def play_game():  # closure
        nonlocal coins
        coins -= 1

        if coins > 1:
            print(f"\n{person} has {coins} coins left.")
        elif coins == 1:
            print(f"\n{person} has {coins} coin left.")
        else:
            print(f"\n{person} is out of coins.")

    return play_game


jenny = parent_funct("Jenny", 2)
tommy = parent_funct("Tommy", 5)
penny = parent_funct("Penny", 3)

jenny()  # Jenny has 1 coin left

tommy()  # Tommy has 4 coins left.
tommy()  # Tommy has 3 coins left.

penny()  # Penny has 2 coins left.
penny()  # Penny has 1 coin left.
penny()  # Penny is out of coins.
