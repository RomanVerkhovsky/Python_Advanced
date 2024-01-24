import script
import gui


def get_field() -> list:
    return script.create_game_field()


def run() -> None:
    gui.view_field()
