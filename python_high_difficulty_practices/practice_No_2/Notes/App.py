from NotesContainer import NotesContainer
import controller


class App:
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
        self.__notes_container = controller.LoadSaver.load(path)

    def create_notes_container(self, path: str) -> None:
        """
        Creating new avoid notes container
        :return:
        """
        self.__notes_container = controller.LoadSaver.create_notes(path)

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
