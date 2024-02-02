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


def read_json(path: str) -> dict:
    with open(path, 'r', encoding='utf8') as file:
        dictionary = json.load(file)
        return dictionary


def is_notes_json(path) -> bool:
    """
    Validate file for compliance with the application format
    :param path: path to notes file
    :return: bool
    """
    notes = read_json(path)

    if len(notes) == 0:
        return False

    for item in notes.items():
        if type(notes[item]) != str:
            return False

    return True


def validate_json(path: str) -> bool:
    """
    Validate path and file
    :param path: path to file
    :return: bool
    """
    if not (check_exist(path) and is_notes_json(path)) is True:
        return False

    return True


def save_notes_json(path: str, notes: dict) -> None:
    with open(path, 'w', encoding='utf8') as file:
        json.dump(notes, file)


def read_last_path() -> str:
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
