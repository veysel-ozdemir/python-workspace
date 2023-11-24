import re
import sys, random
from enum import Enum


class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


def rps():
    game_count = 0
    player_wins = 0
    python_wins = 0

    def play_rps():
        nonlocal player_wins
        nonlocal python_wins

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

        def decide_winner(player, computer):
            nonlocal player_wins
            nonlocal python_wins

            if player == 1 and computer == 3:  # Rock > Scissors
                player_wins += 1
                return "🎉  You win!"
            elif player == 2 and computer == 1:  # Paper > Rock
                player_wins += 1
                return "🎉  You win!"
            elif player == 3 and computer == 2:  # Scissors > Paper
                player_wins += 1
                return "🎉  You win!"
            elif player == computer:
                return "😯  Tie game!"
            else:
                python_wins += 1
                return "🐍  Python wins!"

        game_result = decide_winner(player, computer)

        print(game_result)

        nonlocal game_count
        game_count += 1

        print(f"\n🧮  Game count: {game_count}")
        print(f"👤  Player wins: {player_wins}")
        print(f"🐍  Python wins: {python_wins}")

        print("\n❔  Play again?")

        while True:
            playagain = input("✅  Y for Yes\n❌  N for No\n\n")
            if playagain.lower() not in ["y", "n"]:
                continue
            else:
                break

        if playagain.lower() == "y":
            return play_rps()
        else:
            sys.exit("\n🎉  Thank you for playing!\n👋 See ya!")

    return play_rps


play = rps()
play()
