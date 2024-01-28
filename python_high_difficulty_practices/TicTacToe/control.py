from python_high_difficulty_practices.TicTacToe.gui import gui
from python_high_difficulty_practices.TicTacToe.logic import game_sessions


def info_view_field(field: list) -> None:
    gui.info_view_field(field)


def info_choice_session() -> None:
    gui.info_choice_session()


def info_error_input() -> None:
    gui.info_error_input()


def input_user() -> str:
    return gui.input_user()


class AccessGUI:
    @staticmethod
    def input_user() -> str:
        return input_user()

    @staticmethod
    def info_view_field(field) -> None:
        info_view_field(field)

    @staticmethod
    def info_error_input() -> None:
        info_error_input()

    @staticmethod
    def info_choice_session() -> None:
        info_choice_session()


def run() -> None:
    while True:
        AccessGUI.info_choice_session()
        choice = AccessGUI.input_user()
        if choice == '1':
            game_sessions.game_pc_vs_ai()

        elif choice == '2':
            game_sessions.game_ai_vs_ai()

        elif choice == 'e':
            return
