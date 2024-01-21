import GUI
from App import App
from NotesContainer import NotesContainer
from business_low_level import *
import settings


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
    def save(path: str, id: str, description: str) -> None:
        """
        Save current state of container of notes in notes file
        :param path: path to notes file
        :param id: id note in container (name of note)
        :param description: text of note
        :return: None
        """
        save_notes(path, id, description)

    @staticmethod
    def create_notes(path: str):
        pass


class Accession:
    @staticmethod
    def load_notes(path: str) -> None:
        ClickButton.click_load_notes(path)

    @staticmethod
    def open_notes(id: str) -> str:
        return ClickButton.click_open_notes(id)

    @staticmethod
    def create_note(description: str, id: str) -> None:
        return ClickButton.click_create_note(description, id)

    @staticmethod
    def check_id(id: str) -> bool:
        return ClickButton.check_id(id)

    @staticmethod
    def validate(path) -> bool:
        return ClickButton.validate(path)

    @staticmethod
    def change_path(path: str) -> None:
        ClickButton.change_path(path)


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
    def click_create_note(description: str, id: str) -> None:
        """

        :param description:
        :param id:
        :return:
        """
        app.create_note(description, id)

    @staticmethod
    def validate(path) -> bool:
        """
        Validate path and file
        :param path: path to file
        :return: bool
        """
        return validate(path)

    @staticmethod
    def check_id(id: str) -> bool:
        """
        Checking exist id
        :param id: str
        :return: bool
        """
        return app.get_notes_container().check_id(id)

    @staticmethod
    def change_path(path: str) -> None:
        settings.current_path = path

    def is_container(self) -> bool:
        pass


app = None


def run():
    global app
    app = App()

    gui = GUI.GUI()
    gui.run()
