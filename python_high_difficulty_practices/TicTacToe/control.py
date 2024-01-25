import game_logic
import gui
import game_sessions


def view_field(field: list):
    gui.view_field(field)


def user_input():
    gui.input_user()


class AccessGUI:
    @staticmethod
    def input_request():
        user_input()

    @staticmethod
    def view_field(field):
        view_field(field)


def run() -> None:
    game_sessions.game_pc_and_ai()

