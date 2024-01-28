def info_view_field(field: list) -> None:
    """
    View to console game field
    :return:
    """
    print('_________________')
    for row in range(len(field)):
        print(' ', '  |  '.join(field[row]))
        print('_________________')


def info_error_input() -> None:
    print('Error! Enter a valid value.')


def info_choice_session() -> None:
    print('Choice session of game:\n'
          '  > 1 < - pc vs ai\n'
          '  > 2 < - ai vs ai\n'
          '  > e < - quit\n')


def input_user() -> str:
    return input('Your choice >> ')