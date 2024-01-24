import control


def create_game_field() -> list:
    """
    Creation game field
    :return: avoid game field
    """
    field = []
    for row in range(3):
        field.append([' ', ' ', ' '])

    return field


