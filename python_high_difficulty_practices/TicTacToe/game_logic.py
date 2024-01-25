from decor import *
import control
import asyncio


def create_game_field() -> list:
    """
    Creation game field
    :return: avoid game field
    """
    field = []
    for row in range(3):
        field.append([' ', ' ', ' '])

    return field


def check_movement():
    pass


def check_win():
    pass


@log
def move_player():
    while True:
        control.AccessGUI.input_request()
        break


@log
def move_ai():
    pass


win_combo = [[(0, 0), (0, 1), (0, 2)],
             [(1, 0), (1, 1), (1, 2)],
             [(2, 0), (2, 1), (2, 2)],
             [(0, 0), (1, 0), (2, 0)],
             [(0, 1), (1, 1), (2, 1)],
             [(0, 2), (1, 2), (2, 2)],
             [(0, 0), (1, 1), (2, 2)],
             [(0, 2), (1, 1), (2, 0)]]
