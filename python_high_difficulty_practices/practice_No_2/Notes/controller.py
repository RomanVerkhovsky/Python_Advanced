from python_high_difficulty_practices.practice_No_2.Notes import GUI
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
    def save(path: str, notes: dict) -> None:
        """
        Save current state of container of notes in notes file
        :param path: path to notes file
        :param id: id note in container (name of note)
        :param notes: text of note
        :return: None
        """
        save_notes(path, notes)


class HandlerGUI:

    @staticmethod
    def click_load_notes(notebook: object.__class__, path: str) -> None:
        """
        Loading notes file after pressing the button
        :param notebook: link to object of main class Notebook
        :param path: path to file
        """
        notebook.load_notes_container(path)

    @staticmethod
    def click_open_notes(notebook: object.__class__, id: str) -> tuple:
        """
        Open notes after pressing the button
        :param notebook: link to object of main class Notebook
        :param id: id of note in container
        :return: tuple name of note, text of note
        """
        return notebook.open_note(id)

    @staticmethod
    def click_save_notes(notebook: object.__class__, path: str) -> None:
        """
        Save current state notes
        :param notebook: link to object of main class Notebook
        :param path: is path to file to save
        :return:
        """
        notebook.save_notes(path)

    @staticmethod
    def click_add_note(notebook: object.__class__, content: str, id: str = None) -> None:
        """
        Create note and add note to note container
        :param notebook: link object of main class Notebook
        :param content: text of note
        :param id: name of note
        :return:
        """
        notebook.add_note(content, id)

    @staticmethod
    def get_dict_notes(notebook: object.__class__) -> dict:
        """
        Return notes from container
        :param notebook: link object of main class Notebook
        :return:
        """
        return notebook.get_dictionary_notes()

    @staticmethod
    def validate(path) -> bool:
        """
        Validate path and file
        :param path: path to file
        :return: bool
        """
        return validate(path)

    @staticmethod
    def check_id(notebook: object.__class__, id: str) -> bool:
        """
        Checking exist id
        :param notebook: link to object of main class Notebook
        :param id: name of note
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
    def load_notes(notebook: object, path: str) -> None:
        HandlerGUI.click_load_notes(notebook, path)

    @staticmethod
    def open_notes(notebook: object, id: str) -> tuple:
        return HandlerGUI.click_open_notes(notebook, id)

    @staticmethod
    def save_notes(notebook: object, path: str) -> None:
        HandlerGUI.click_save_notes(notebook, path)

    @staticmethod
    def add_note(notebook: object, description: str, id: str) -> None:
        return HandlerGUI.click_add_note(notebook, description, id)

    @staticmethod
    def get_dict_notes(notebook: object) -> dict:
        return HandlerGUI.get_dict_notes(notebook)

    @staticmethod
    def check_id(notebook: object, id: str) -> bool:
        return HandlerGUI.check_id(notebook, id)

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
