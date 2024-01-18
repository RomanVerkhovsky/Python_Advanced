from Note import Note


class NotesContainer:
    """Class to storage loaded list of notes"""
    def __init__(self) -> None:
        self.__count = 0
        self.__notes = {}

    def get_count(self) -> int:
        """
        Returning count of notes in container
        :return: int
        """
        return self.__count

    def get_dict(self) -> dict:
        """
        Returning object class Dict contain object class Notes
        :return: dict
        """
        return self.__notes

    def add_note(self, description: str, id: str = None) -> None:
        """
        Adding note in opened list of notes
        :param description:
        :param id:
        :return:
        """
        if id is None:
            id = str(self.__count + 1)

        note = Note(id, description)
        self.__notes[id] = note
        self.__count += 1

    def remove_note(self, id: str) -> None:
        """
        Removing a note from opened list of notes
        :param id: key in list of notes
        :return:
        """
        if id in self.__notes:
            del self.__notes[id]
            self.__count -= 1
