import sys
from rps import rps
from guess_number import guess_number


def arcade(name="Player", initialentry=True):
    if initialentry:
        print(f"🤖  {name}, welcome to the Arcade!")

    welcome_back = False

    while True:
        if welcome_back:
            print(f"🤖  Welcome back to the Arcade menu, {name}!\n")

        player_choice = input(
            "\n🎮  Please enter ...\n    1 for Rock-Paper-Scissors game,\n    2 for Guess My Number game, \n\n🔚  Or press 'x' for exit the Arcade:\n\n"
        )

        if player_choice not in ["1", "2", "x", "X"]:
            print(f"\n❗  {name}, please enter 1, 2, or x.")
            return arcade(name, False)

        welcome_back = True

        if player_choice == "1":
            rock_paper_scissors = rps(name)
            rock_paper_scissors()
        elif player_choice == "2":
            guess_my_number = guess_number(name)
            guess_my_number()
        else:
            sys.exit(f"\n👋  See you next time, {name}!")


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

    arcade(args.name)
