from python_high_difficulty_practices.TicTacToe.gui import gui
from python_high_difficulty_practices.TicTacToe.logic import game_sessions
import asyncio


def info_view_field(field: list) -> None:
    """
    Displaying the game field
    :param field: created game field
    :return:
    """
    gui.info_view_field(field)


def info_choice_session() -> None:
    """
    Displaying main menu
    :return:
    """
    gui.info_choice_session()


def info_error_input() -> None:
    """
    Info error after entered a valid value
    :return:
    """
    gui.info_error_input()


def info_win(current_player: str) -> None:
    """
    Displaying info about winner
    :param current_player: name of winner
    :return:
    """
    gui.info_win(current_player)


def info_draw() -> None:
    """
    Display info about draw
    :return:
    """
    gui.info_draw()


def input_user() -> str:
    """
    Input request
    :return: str
    """
    return gui.input_user()


class AccessGUI:
    @staticmethod
    def input_user() -> str:
        return input_user()

    @staticmethod
    def info_view_field(field: list) -> None:
        info_view_field(field)

    @staticmethod
    def info_error_input() -> None:
        info_error_input()

    @staticmethod
    def info_choice_session() -> None:
        info_choice_session()

    @staticmethod
    def info_win(current_player: str) -> None:
        info_win(current_player)

    @staticmethod
    def info_draw() -> None:
        info_draw()


def run() -> None:
    """
    Starting the game
    :return:
    """
    # main game loop
    while True:
        # menu display
        AccessGUI.info_choice_session()

        choice = AccessGUI.input_user()
        if choice == '1':
            asyncio.run(game_sessions.game_pc_vs_ai())

        elif choice == '2':
            asyncio.run(game_sessions.game_pc_vs_pc())

        elif choice == '3':
            asyncio.run(game_sessions.game_ai_vs_ai())

        elif choice == 'q':
            return
