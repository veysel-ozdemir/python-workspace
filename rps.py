import re
import sys, random
from enum import Enum


class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


def play_rps():
    player_choice = input(
        "\n🎮  Enter ...\n🪨   1 for Rock,\n🧻  2 for Paper, \n✂️   3 for Scissors:\n\n"
    )

    if player_choice not in ["1", "2", "3"]:
        print("\n❗  You must enter 1, 2, or 3.")
        return play_rps()

    player = int(player_choice)

    computer_choice = random.choice("123")
    computer = int(computer_choice)

    print(f"\nYou chose {RPS(player).name}.")
    print(f"Python chose {RPS(computer).name}.\n")

    if player == 1 and computer == 3:  # Rock > Scissors
        print("🎉  You win!")
    elif player == 2 and computer == 1:  # Paper > Rock
        print("🎉  You win!")
    elif player == 3 and computer == 2:  # Scissors > Paper
        print("🎉  You win!")
    elif player == computer:
        print("😯  Tie game!")
    else:
        print("🐍  Python wins!")

    print("\n❔  Play again?")

    while True:
        playagain = input("\n✅  Y for Yes\n❌  N for No\n\n")
        if playagain.lower() not in ["y", "n"]:
            continue
        else:
            break

    if playagain.lower() == "y":
        return play_rps()
    else:
        sys.exit("\n🎉  Thank you for playing!\n👋 See ya!")


play_rps()
