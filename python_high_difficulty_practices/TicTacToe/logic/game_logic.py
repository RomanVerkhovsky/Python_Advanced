from python_high_difficulty_practices.TicTacToe import control
from python_high_difficulty_practices.TicTacToe.logic.decor import *
import random
import os
import asyncio


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


def current_player_container(current_player: str, x_player: list, o_player: list) -> list:
    """
    Change player container for checking to win
    :param current_player: sign current player
    :param x_player: container - list of moves
    :param o_player: container - list of moves
    :return: container of current player
    """
    if current_player == 'x':
        return x_player

    elif current_player == 'o':
        return o_player


def change_player(current_player: str) -> str:
    """
    Change player before next move
    :param current_player: sign of current player
    :return: next current player
    """
    if current_player == 'x':
        return 'o'

    elif current_player == 'o':
        return 'x'


def is_end_game(field: list) -> bool:
    """
    Checking for draw. If there are empty cells on the field return False, else True
    :param field: created game field
    :return: bool
    """
    for i in field:
        if ' ' in i:
            return False

    return True


def check_select(select: str, field: list) -> bool:
    """

    :param select:
    :param field:
    :return:
    """
    field = sum(field, [])

    if select.isdigit():
        if 1 <= int(select) <= 9 and field[int(select) - 1] == ' ':
            return True

    return False


def update_state_game(select: str, field: list, player: list, current_player: str) -> None:
    if 1 <= int(select) <= 3:
        player.append((0, int(select) - 1))
        field[0][int(select) - 1] = current_player

    elif 4 <= int(select) <= 6:
        player.append((1, int(select) - 4))
        field[1][int(select) - 4] = current_player

    elif 7 <= int(select) <= 9:
        player.append((2, int(select) - 7))
        field[2][int(select) - 7] = current_player


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
async def move_player(field: list) -> str:

    while True:
        select = control.AccessGUI.input_user()
        if select == 'q' or check_select(select, field) is True:
            return select

        else:
            control.AccessGUI.info_error_input()


@log
async def move_ai(field: list) -> str:

    await asyncio.sleep(2)
    while True:
        select = str(random.randint(0, 8))
        if check_select(select, field):
            return select
