def info_view_field(field: list) -> None:
    """
    View to console game field
    :return:
    """
    field_2 = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]

    print('_________________', '     _________________')
    for row in range(len(field)):
        print(' ', '  |  '.join(field[row]), '        ', '  |  '.join(field_2[row]))
        print('_________________', '     _________________')


def info_error_input() -> None:
    print('Error! Enter a valid value.\n'
          'Select a number or <q> for quit to main menu..')


def info_choice_session() -> None:
    print('Choice session of game:\n\n'
          '  > 1 < - pc vs ai\n'
          '  > 2 < - pc vs pc\n'
          '  > 3 < - ai vs ai\n'
          '  > q < - quit\n')


def info_win(current_player: str) -> None:
    print(f'\n        >> Player - {current_player} WIN <<\n'
          f'\nPress Enter to return main menu..')


def info_draw() -> None:
    print('DRAW! Press Enter to return main menu..')


def input_user() -> str:
    return input('>> ')
