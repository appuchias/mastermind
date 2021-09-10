import random, argparse


def get_ai_code():
    numbers = list(range(10))
    random.shuffle(numbers)

    code = numbers[:4]

    return code


def play_game(turns: int, mode: str):
    ai_code = get_ai_code()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "-t",
        "--turns",
        help="Select the number of turns available",
        type=int,
        default=12,
    )
    parser.add_argument(
        "-m",
        "--mode",
        help="Game mode",
        choices=["1-player", "2-player"],
        default="1-player",
    )

    args = parser.parse_args()

    print(args)

    play_game()
