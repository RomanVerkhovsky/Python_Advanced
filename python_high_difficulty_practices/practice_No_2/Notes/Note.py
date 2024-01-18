class Note:
    """Class to creating note"""
    def __init__(self, id: str, description: str) -> None:
        self.__id = id
        self.__description = description

    def get_id(self) -> str:
        """
        Returning name of note
        :return: str
        """
        return self.__id

    def get_description(self) -> str:
        """
        Returning text of note
        :return: str
        """
        return self.__description

    def edit(self, description: str) -> None:
        """
        Editing note
        :param description: new text of note
        :return: str
        """
        self.__description = description
