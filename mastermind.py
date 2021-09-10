"""This is the classic mastermind game. Adapted for playing through command-line or using a GUI thanks to pygame. Work in progress."""

import random, argparse


def parse_args() -> argparse.Namespace:
    """Gets CL arguments for game. Returns a Namespace object with t and p values meaning turns and players"""
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "-t",
        metavar="turns",
        help="Select the number of turns available",
        type=int,
        default=12,
    )
    parser.add_argument(
        "-p",
        metavar="players",
        help="Select number of players for this game (1 or 2)",
        choices=[1, 2],
        default=1,
    )

    args = parser.parse_args()

    return args


def get_ai_code() -> list[int]:
    """Randomizes ai code"""
    numbers = list(range(10))
    random.shuffle(numbers)

    code = numbers[:4]

    return code


def get_user_input(turn: int) -> list[int]:
    is_user_input_valid = False
    while not is_user_input_valid:
        user_code = (
            input(f"This is turn {turn}. Please inut your guess (4 digits):\n> ")
            .strip()
            .replace(" ", "")
        )
        if len(user_code) == 4 and user_code.isdigit():
            is_user_input_valid = True
        else:
            print("Your input was not valid.")

    user_code = [int(n) for n in list(user_code)]

    return user_code


def check_codes(ai: list[int], user: list[int]) -> tuple[int, int]:
    """Checks amount of numbers and placement correct in the user code. Returns in format (hurt, dead)"""
    hurt = 0  # Correct number, incorrect placement
    dead = 0  # Correct number,   correct placement

    for idx, n in enumerate(ai):
        if user[idx] == n:
            dead += 1

    for n in user:
        if n in ai:
            hurt += 1

    hurt -= dead

    return hurt, dead

    # TODO: Transfer info to dict to avoid repetitions
    """
    [7, 4, 1, 6]
    - - -
    [4, 4, 4, 4]
    *3h, 1d* -> 0h, 1d
    """


def play_game(turns: int, players: int):
    is_game_finished = lambda x, y: x == y

    if players == 1:
        ai_code = get_ai_code()
        # print(ai_code)

        for turn in range(1, turns + 1):
            user_code = get_user_input(turn)
            if is_game_finished(ai_code, user_code):
                print(f"You've won. The code was: {ai_code}")
                return True
            code_status = check_codes(ai_code, user_code)
            # print(user_code)
            print(f"{code_status[0]}h, {code_status[1]}d")
        else:
            print(f"You lost. You ran out of turns. Code was: {ai_code}")
            return False

    elif players == 2:
        ...

    else:
        print("Invalid value reached function")


if __name__ == "__main__":
    args = parse_args()

    play_game(args.t, args.p)  # Starts a game with specific turns and players
