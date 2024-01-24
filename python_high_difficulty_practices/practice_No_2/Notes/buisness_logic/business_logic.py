import os


def check_exist(path) -> bool:
    """
    Checking exist file to path
    :param path: is path to file
    :return: bool
    """
    return os.path.exists(path)


def is_notes(path) -> bool:
    """
    Validate file for compliance with the application format
    :param path: path to notes file
    :return: bool
    """
    text = read_notes(path)

    if len(text) == 0:
        return False

    array = text.split('\n')
    for i in range(len(array)):
        note = array[i].split(':')
        if len(note) != 2:
            return False

    return True


def validate(path: str) -> bool:
    """
    Validate path and file
    :param path: path to file
    :return: bool
    """
    if not (check_exist(path) and is_notes(path)) is True:
        return False

    return True


def read_notes(path) -> str:
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
    text = read_notes(path)

    dictionary = {}
    array = text.split('\n')
    for i in range(len(array)):
        note = array[i].split(':')
        dictionary[note[0]] = note[1]

    return dictionary


def write_file(path, text) -> None:
    file = open(path, 'w', encoding='utf8')
    file.write(text)
    file.close()


def create_to_write(dictionary: dict) -> str:
    """
    Preparing to write
    :param dictionary: is dictionary of notes
    :return: is notes in str
    """
    array = []
    for items in dictionary.items():
        array.append(':'.join([items[0], items[1]]))

    text = '\n'.join(array)

    return text


def save_notes(path: str, notes: dict) -> None:
    notes = create_to_write(notes)
    write_file(path, notes)


def handling_entry(text: str):
    if len(text) == 0:
        return

    array = []
    pass

