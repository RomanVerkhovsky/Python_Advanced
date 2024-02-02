import os
import json


# for json
def check_exist(path) -> bool:
    """
    Checking exist file to path
    :param path: is path to file
    :return: bool
    """
    return os.path.exists(path)


def read(path: str) -> dict:
    """
    Reading json file
    :param path: path to file
    :return: dictionary
    """
    with open(path, 'r', encoding='utf8') as file:
        dictionary = json.load(file)
        return dictionary


def is_notes(path) -> bool:
    """
    Validate file for compliance with the application format
    :param path: path to notes file
    :return: bool
    """
    notes = read(path)

    if len(notes) == 0:
        return False

    for item in notes.items():
        if type(notes[item]) != str:
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


def save_notes(path: str, notes: dict) -> None:
    """
    Save all changes in notes
    :param path: path to save
    :param notes: dictionary of notes
    :return:
    """
    with open(path, 'w', encoding='utf8') as file:
        json.dump(notes, file)


def open_last_file() -> str:
    """
    Reading last path to notes file from settings
    :return: path
    """
    with open('data/settings.json', 'r', encoding='utf8') as file:
        settings = json.load(file)
        path = settings['current_path']
        return path


def change_current_path(path: str) -> None:
    """
    Change current path in settings to last opened path to notes file
    :param path: path to notes file
    :return:
    """
    with open('data/settings.json', 'r', encoding='utf8') as file:
        settings = json.load(file)
        settings['current_path'] = path

    with open('data/settings.json', 'w') as file:
        json.dump(settings, file)
