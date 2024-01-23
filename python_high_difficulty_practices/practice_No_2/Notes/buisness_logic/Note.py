class Note:
    """Class to creating note"""
    def __init__(self, id: str, content: str) -> None:
        self.__id = id
        self.__content = content

    def get_id(self) -> str:
        """
        Returning name of note
        :return: str
        """
        return self.__id

    def get_content(self) -> str:
        """
        Returning text of note
        :return: str
        """
        return self.__content

    def edit(self, content: str) -> None:
        """
        Editing note
        :param content: new text of note
        :return: str
        """
        self.__content = content
