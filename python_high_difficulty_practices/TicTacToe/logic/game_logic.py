from python_high_difficulty_practices.TicTacToe import control
from python_high_difficulty_practices.TicTacToe.logic.decor import *
import random
import os


def clear_console():
    os.system('cls')


def create_game_field() -> list:
    """
    Creation game field
    :return: avoid game field
    """
    field = []
    for row in range(3):
        field.append([' ', ' ', ' '])

    return field


def change_player(current_player: str) -> str:
    if current_player == 'x':
        return 'o'

    elif current_player == 'o':
        return 'x'


def is_end_game(field: list) -> bool:
    count = 0
    for i in field:
        if i == 'x' or i == 'o':
            count += 1

    if count == 9:
        return True

    return False


def check_select(select: str, field: list) -> bool:
    field = sum(field, [])

    if select.isdigit():
        if 0 <= int(select) <= 8 and field[int(select)] == ' ':
            return True

    return False


def update_state_game(select: str, field: list, player: list, current_player: str) -> None:
    if 0 <= int(select) <= 2:
        player.append((0, int(select)))
        field[0][int(select)] = current_player

    elif 3 <= int(select) <= 5:
        player.append((1, int(select) - 3))
        field[1][int(select) - 3] = current_player

    elif 6 <= int(select) <= 8:
        player.append((2, int(select) - 6))
        field[2][int(select) - 6] = current_player


def check_win(player: list) -> bool:
    win_combo = [[(0, 0), (0, 1), (0, 2)],
                 [(1, 0), (1, 1), (1, 2)],
                 [(2, 0), (2, 1), (2, 2)],
                 [(0, 0), (1, 0), (2, 0)],
                 [(0, 1), (1, 1), (2, 1)],
                 [(0, 2), (1, 2), (2, 2)],
                 [(0, 0), (1, 1), (2, 2)],
                 [(0, 2), (1, 1), (2, 0)]]

    for i in range(len(win_combo)):
        if win_combo[i][0] in player and win_combo[i][1] in player and win_combo[i][2] in player:
            return True

    return False


@log
def move_player(field: list) -> str:

    while True:
        select = control.AccessGUI.input_user()
        if check_select(select, field) is True:
            return select

        else:
            control.AccessGUI.info_error_input()


@log
def move_ai(field: list) -> str:

    while True:
        select = str(random.randint(0, 8))
        if check_select(select, field):
            return select
