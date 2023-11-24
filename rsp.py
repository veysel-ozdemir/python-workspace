import sys, random
from enum import Enum


class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


while True:
    player_choice = input(
        "\nEnter ...\n1 for Rock,\n2 for Paper, \n3 for Scissors:\nE for Exit:\n\n"
    )

    if player_choice == "E":
        sys.exit("👋 See ya!")

    player = int(player_choice)
    if player < 1 or player > 3:
        sys.exit("You must enter 1, 2, or 3.")

    computer_choice = random.choice("123")
    computer = int(computer_choice)

    print(f"\nYou chose {RPS(player).name}.")
    print(f"Python chose {RPS(computer).name}.\n")

    if player == 1 and computer == 3:  # Rock > Scissors
        print("🎉 You win!")
    elif player == 2 and computer == 1:  # Paper > Rock
        print("🎉 You win!")
    elif player == 3 and computer == 2:  # Scissors > Paper
        print("🎉You win!")
    elif player == computer:
        print("😯 Tie game!")
    else:
        print("🐍 Python wins!")
