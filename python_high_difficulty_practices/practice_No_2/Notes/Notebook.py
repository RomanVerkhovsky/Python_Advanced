from python_high_difficulty_practices.practice_No_2.Notes.buisness_logic.NotesContainer import NotesContainer
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

    def load_notes_container(self, path: str) -> None:
        """
        Load container of notes in application
        :param path: path to notes file
        :return:
        """
        self.__notes_container = controller.SaveLoader.load(path)

    def save_notes(self, path: str, id: str) -> None:
        """
        Save current state of container of notes in notes file
        :param path: path to notes file
        :param id: id note in container
        :return: None
        """
        description = self.__notes_container.get_dict()[id].get_description()
        controller.SaveLoader.save(path, id, description)

    # def create_notes_container(self, path: str) -> None:
    #     """
    #     Creating new avoid notes container
    #     :return:
    #     """
    #     self.__notes_container = controller.SaveLoader.create_notes(path)

    def create_note(self, description: str, id: str = None):
        """
        Creating a note in the current container
        :param description: text of note
        :param id: name of note
        :return:
        """
        self.__notes_container.add_note(description, id)

    def delete_note(self, id: str) -> None:
        """
        Deleting a note in the current container
        :param id:
        :return:
        """
        if id not in self.__notes_container:
            return

        self.__notes_container.remove_note(id)

    def open_note(self, id: str) -> str:
        """

        :param id:
        :return: str
        """
        return self.__notes_container.get_dict()[id].get_description()

    def search_note(self): pass
