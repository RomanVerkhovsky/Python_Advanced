from python_high_difficulty_practices.practice_No_2.Notes.buisness_logic.Note import Note


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

    def get_dict_notes(self) -> dict:
        """
        Returning object class Dict contain object class Notes
        :return: dict
        """
        return self.__notes

    def add_note(self, content: str, id: str) -> None:
        """
        Adding note in opened list of notes.
        If id is not specified, the text of the note is used to create id
        :param content: text from note
        :param id: id from note
        :return:
        """
        if id == '':
            if len(content) != 0:
                create_id = content.split(' ')
                id = create_id[0]
                if len(id) > 10:
                    id = id[0:10:1]

        note = Note(id, content)
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

    def check_id(self, id: str) -> bool:
        """
        Checking id in notes
        :param id: str
        :return: bool
        """
        if id in self.__notes:
            return True

        return False
