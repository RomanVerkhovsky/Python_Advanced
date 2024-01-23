from python_high_difficulty_practices.practice_No_2.Notes.gui import GUI
from Notebook import Notebook
from python_high_difficulty_practices.practice_No_2.Notes.buisness_logic.NotesContainer import NotesContainer
from python_high_difficulty_practices.practice_No_2.Notes.buisness_logic.business_logic import *
from python_high_difficulty_practices.practice_No_2.Notes.buisness_logic import settings


class SaveLoader:

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


class HandlerGUI:

    @staticmethod
    def click_load_notes(path: str, notebook: object.__class__) -> None:
        """
        Loading notes file after pressing the button
        :param notebook:
        :param path: path to file
        """
        notebook.load_notes_container(path)

    @staticmethod
    def click_open_notes(id: str, notebook: object.__class__) -> str:
        """
        Open notes after pressing the button
        :param notebook:
        :param id: id of note in container
        :return: text of note
        """
        return notebook.open_note(id)

    @staticmethod
    def click_create_note(description: str, id: str, notebook: object.__class__) -> None:
        """

        :param notebook:
        :param description:
        :param id:
        :return:
        """
        notebook.create_note(description, id)

    @staticmethod
    def validate(path) -> bool:
        """
        Validate path and file
        :param path: path to file
        :return: bool
        """
        return validate(path)

    @staticmethod
    def check_id(id: str, notebook: object.__class__) -> bool:
        """
        Checking exist id
        :param notebook:
        :param id: str
        :return: bool
        """
        return notebook.get_notes_container().check_id(id)

    @staticmethod
    def change_path(path: str) -> None:
        settings.current_path = path

    def is_container(self) -> bool:
        pass


class Accession:

    @staticmethod
    def load_notes(path: str, notebook: object) -> None:
        HandlerGUI.click_load_notes(path, notebook)

    @staticmethod
    def open_notes(id: str, notebook: object) -> str:
        return HandlerGUI.click_open_notes(id, notebook)

    @staticmethod
    def create_note(description: str, id: str, notebook: object) -> None:
        return HandlerGUI.click_create_note(description, id, notebook)

    @staticmethod
    def check_id(id: str, notebook: object) -> bool:
        return HandlerGUI.check_id(id, notebook)

    @staticmethod
    def validate(path) -> bool:
        return HandlerGUI.validate(path)

    @staticmethod
    def change_path(path: str) -> None:
        HandlerGUI.change_path(path)


def run():
    notebook = Notebook()

    gui = GUI.GUI(notebook)
    gui.run()
