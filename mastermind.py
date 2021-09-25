"""This is the classic mastermind game. Adapted for playing through command-line or using a GUI thanks to pygame. Work in progress."""

import random, argparse
from getpass import getpass


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
        choices=["1", "2"],
        default="1",
    )

    args = parser.parse_args()

    return args


def get_ai_code() -> list[int]:
    """Randomizes ai code"""
    numbers = list(range(10))
    random.shuffle(numbers)

    code = numbers[:4]

    return code


def get_user_input(turn: int, player: int = 0) -> list[int]:
    is_user_input_valid = False
    while not is_user_input_valid:
        user_code = (
            input(
                "\n------------\nThis is turn"
                f" {turn}{f' for player {player}' if player else ''}. Please inut your"
                " guess (4 digits):\n> "
            )
            .strip()
            .replace(" ", "")
        )
        if len(set(user_code)) == 4 and user_code.isdigit():
            is_user_input_valid = True
        else:
            print("Your input was not valid.")

    user_code = [int(n) for n in list(user_code)]

    return user_code


def check_codes(ai: list[int], user: list[int]) -> tuple[int, int]:
    """Checks amount of numbers and placement correct in the user code. Returns in format (hurt, dead)"""

    codes_status = {"hurt": [], "dead": []}

    for idx in range(4):
        if user[idx] == ai[idx]:
            codes_status["dead"].append(user[idx])

    for n in user:
        if n in ai and n not in codes_status["dead"]:
            codes_status["hurt"].append(n)

    hurt, dead = [len(codes_status[key]) for key in codes_status.keys()]

    # Hurt are wrong placed numbers and dead are correct numbers in correct positions
    return hurt, dead


def get_users_code() -> list[list[int]]:
    codes = []
    for player in range(2):
        is_user_input_valid = False
        while not is_user_input_valid:
            hidden_code = (
                getpass(
                    f"\n------------\nInput your hidden code, player {player+1}. 4"
                    " digits, no spaces. You won't see it appear on screen, but it"
                    " will be registered.\n> "
                )
                .strip()
                .replace(" ", "")
            )
            if len(set(hidden_code)) == 4 and hidden_code.isdigit():
                is_user_input_valid = True
            else:
                print("Your input was not valid.")

        hidden_code = [int(n) for n in list(hidden_code)]

        codes.append(hidden_code)
        print(hidden_code)

    assert len(codes) == 2

    return codes


def play_game(turns: int, players: int):
    is_game_finished = lambda x, y: x == y

    if players == 1:
        ai_code = get_ai_code()
        print(ai_code)

        for turn in range(1, turns + 1):
            user_code = get_user_input(turn)
            if is_game_finished(ai_code, user_code):
                print(f"\n------------\nYou've won. The code was: {ai_code}")
                return True
            code_status = check_codes(ai_code, user_code)
            # print(user_code)
            print(f"{code_status[0]}h, {code_status[1]}d")
        else:
            print(f"You lost. You ran out of turns. Code was: {ai_code}")
            return False

    elif players == 2:
        codes = get_users_code()

        for turn in range(1, turns + 1):
            for player in range(1, 3):
                user_code = get_user_input(turn, player)
                if is_game_finished(codes[2 - player], user_code):
                    print(f"You've won. The code was: {ai_code}")
                    return True
                code_status = check_codes(codes[2 - player], user_code)
                print(f"{code_status[0]}h, {code_status[1]}d")
        else:
            for player in range(1, 3):
                print(
                    f"You lost, player {player}. You ran out of turns. Code was:"
                    f" {codes[2 - player]}"
                )
            return False

    else:
        print("Invalid value reached function")


if __name__ == "__main__":
    args = parse_args()

    if args.p.isdigit():
        players = int(args.p)
    else:
        raise ValueError("Could not convert players to int")

    play_game(args.t, players)  # Starts a game with specific turns and players
