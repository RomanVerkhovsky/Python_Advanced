import GUI
from App import App
from NotesContainer import NotesContainer
from business_low_level import *


class Accession:
    @staticmethod
    def load_notes(path: str) -> None:
        ClickButton.click_load_notes(path)

    @staticmethod
    def open_notes(id: str) -> str:
        return ClickButton.click_open_notes(id)

    @staticmethod
    def validate(path) -> bool:
        return ClickButton.validate(path)


class LoadSaver:
    @staticmethod
    def load(path: str) -> object:
        """
        Loading container of notes in application
        :param path: path to file
        :return: object class NotesContainer
        """
        dictionary = create_dict(path)
        container = NotesContainer()

        for key in dictionary:
            container.add_note(dictionary[key], key)

        return container

    @staticmethod
    def save():
        pass


class ClickButton:
    @staticmethod
    def click_load_notes(path: str) -> None:
        """
        Loading notes file after pressing the button
        :param path: path to file
        """
        app.load_notes_container(path)

    @staticmethod
    def click_open_notes(id: str) -> str:
        """
        Open notes after pressing the button
        :param id: id of note in container
        :return: text of note
        """
        return app.open_note(id)

    @staticmethod
    def validate(path) -> bool:
        """
        Validate path and file
        :param path: path to file
        :return: bool
        """
        return validate(path)


app = App()


def run():
    gui = GUI.GUI()
    gui.run()
