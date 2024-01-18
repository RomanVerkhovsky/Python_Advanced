import GUI
from App import App
from NotesContainer import NotesContainer
from business_low_level import *


class HandlerLoadSave:
    @staticmethod
    def load(path: str) -> object:
        """

        :param path:
        :return:
        """
        dictionary = create_dict(path)
        container = NotesContainer()

        for key in dictionary:
            container.add_note(dictionary[key], key)

        return container

    @staticmethod
    def save():
        pass


class HandlerButton:
    @staticmethod
    def click_load_notes(path: str):
        """

        :param path:
        :return:
        """
        app.load_notes_container(path)

    @staticmethod
    def click_open_notes(id: str) -> str:
        """

        :param id:
        :return:
        """
        return app.open_note(id)


app = App()


def run():
    gui = GUI.GUI()
    gui.run()
