from python_high_difficulty_practices.practice_No_2.Notes.buisness_logic.NotesContainer import NotesContainer
from python_high_difficulty_practices.practice_No_2.Notes.buisness_logic.Note import Note
import controller


class Notebook:
    """Main class for working with notes"""
    def __init__(self) -> None:
        self.__notes_container = NotesContainer()

    def get_notes_container(self) -> object:
        """
        Returning object class NotesContainer
        :return: object
        """
        return self.__notes_container

    def get_dictionary_notes(self) -> dict:
        dictionary = {}
        for item in self.__open_container().items():
            dictionary[item[1].get_id()] = item[1].get_content()
        return dictionary

    def load_notes_container(self, path: str) -> None:
        """
        Load container of notes in application
        :param path: path to notes file
        :return:
        """
        self.__notes_container = controller.SaveLoader.load(path)

    def __open_container(self) -> dict:
        return self.__notes_container.get_dict_notes()

    def get_note(self, id: str) -> object:
        return self.__notes_container.get_dict_notes()[id]

    def save_notes(self, path) -> None:
        """
        Save current state of container of notes in notes file
        :param path: path to notes file
        :return: None
        """

        list_notes = self.__open_container()

        dictionary = {}
        for item in list_notes.items():
            dictionary[item[0]] = item[1].get_content()

        controller.SaveLoader.save(path, dictionary)


    # def create_notes_container(self, path: str) -> None:
    #     """
    #     Creating new avoid notes container
    #     :return:
    #     """
    #     self.__notes_container = controller.SaveLoader.create_notes(path)

    def add_note(self, content: str, id: str = None):
        """
        Creating a note in the current container
        :param content: text of note
        :param id: name of note
        :return:
        """
        self.__notes_container.add_note(content, id)

    def del_note(self, id: str) -> None:
        """
        Deleting a note in the current container
        :param id:
        :return:
        """
        if id not in self.__notes_container:
            return

        self.__notes_container.remove_note(id)

    def open_note(self, id: str) -> tuple:
        """
        Return tuple (name, content) from Note object
        :param id: id of notes in container
        :return: tuple (name, content)
        """
        name = self.__open_container()[id].get_id()
        description = self.__open_container()[id].get_content()
        return name, description

    def search_note(self): pass

    def check_id(self, id: str) -> bool:
        if id in self.__open_container():
            return True
        return False
