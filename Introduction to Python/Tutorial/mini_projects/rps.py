import sys, random
from enum import Enum


def rps(name="Player"):
    game_count = 0
    player_wins = 0
    python_wins = 0

    print(f"👾  Welcome to the Rock-Paper-Scissors game, {name}!")

    def play_rps():
        nonlocal name
        nonlocal player_wins
        nonlocal python_wins

        class RPS(Enum):
            ROCK = 1
            PAPER = 2
            SCISSORS = 3

        player_choice = input(
            f"\n🎮  {name}, please enter ...\n🪨   1 for Rock,\n🧻  2 for Paper, \n✂️   3 for Scissors:\n\n"
        )

        if player_choice not in ["1", "2", "3"]:
            print(f"\n❗  {name}, please enter 1, 2, or 3.")
            return play_rps()

        player = int(player_choice)

        computer_choice = random.choice("123")
        computer = int(computer_choice)

        print(f"\n{name}, you chose {RPS(player).name}.")
        print(f"Python chose {RPS(computer).name}.\n")

        def decide_winner(player, computer):
            nonlocal name
            nonlocal player_wins
            nonlocal python_wins

            if player == 1 and computer == 3:  # Rock > Scissors
                player_wins += 1
                return f"🎉  {name} wins!"
            elif player == 2 and computer == 1:  # Paper > Rock
                player_wins += 1
                return f"🎉  {name} wins!"
            elif player == 3 and computer == 2:  # Scissors > Paper
                player_wins += 1
                return f"🎉  {name} wins!"
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
        print(f"🥳  {name} wins: {player_wins}")
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
            print(f"\n🎉  Thank you for playing! 🎉\n")
            if __name__ == "__main__":
                sys.exit(f"\n👋  See you, {name}!")
            else:
                return

    return play_rps


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

    rock_paper_scissors = rps(args.name)
    rock_paper_scissors()
