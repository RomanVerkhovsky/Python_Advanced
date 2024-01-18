def read_list_notes(path) -> str:
    """
    Reading file
    :param path: path to notes file
    :return: str
    """
    file = open(path, 'r', encoding='utf8')
    text = file.read()
    file.close()
    return text


def create_dict(path) -> dict:
    """
    Converting .txt file in dict
    :param path: path to notes file
    :return: dict
    """
    text = read_list_notes(path)

    if not is_notes():
        raise ValueError('is not notes!')

    dictionary = {}
    array = text.split('\n')
    for i in range(len(array)):
        note = array[i].split(':')
        dictionary[note[0]] = note[1]

    return dictionary


def handling_entry(text: str):
    if len(text) == 0:
        return

    array = []
    pass


def save_note(): pass


def is_notes() -> bool:
    """

    :return:
    """
    return True

