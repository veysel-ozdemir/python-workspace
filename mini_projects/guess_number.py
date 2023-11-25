import sys, random as rdm


def guess_number(name="Player"):
    game_count = 0
    player_wins = 0

    print(f"👾  Welcome to the Guess My Number game, {name}!")

    def play_guess_number():
        nonlocal name
        nonlocal game_count
        nonlocal player_wins

        player_choice = input(
            f"\n🎮  {name}, guess which number I'm thinking of... 1, 2, or 3.\n\n"
        )

        if player_choice not in ["1", "2", "3"]:
            print(f"\n❗  {name}, please enter 1, 2, or 3.")
            return play_guess_number()

        player = int(player_choice)

        computer_choice = rdm.choice("123")
        computer = int(computer_choice)

        print(f"\n{name}, you chose {player}.")
        print(f"I was thinking about the number {computer_choice}.\n")

        def decide_winner(player, computer):
            nonlocal name
            nonlocal player_wins

            if player == computer:
                player_wins += 1
                return f"🎉  {name} wins!"
            else:
                return f"😢  Sorry, {name}. Better luck next time! 🍀"

        game_result = decide_winner(player, computer)

        print(game_result)

        nonlocal game_count
        game_count += 1

        print(f"\n🧮  Game count: {game_count}")
        print(f"🥳  {name} wins: {player_wins}")
        print(f"➗  Your winning percentage: {player_wins/game_count:.2%}")

        print(f"\n❔  Play again, {name}?")

        while True:
            playagain = input("✅  Y for Yes\n❌  N for No\n\n")
            if playagain.lower() not in ["y", "n"]:
                continue
            else:
                break

        if playagain.lower() == "y":
            return play_guess_number()
        else:
            print(f"\n🎉  Thank you for playing! 🎉\n")
            if __name__ == "__main__":
                sys.exit(f"\n👋  See you, {name}!")
            else:
                return

    return play_guess_number


if __name__ == "__main__":
    # command-line interface
    import argparse

    parser = argparse.ArgumentParser(
        description="Provides a personalized game experience.",
    )

    parser.add_argument(
        "-n",
        "--name",
        metavar="name",
        required=True,
        help="The name of the person playing the game.",
    )

    args = parser.parse_args()

    guess_my_number = guess_number(args.name)
    guess_my_number()
