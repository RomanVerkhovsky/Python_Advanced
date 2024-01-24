import os
import control


def view_field() -> None:
    """
    View to console game field
    :return:
    """
    field = control.get_field()

    field[0][0] = 'x'
    field[1][1] = 'o'
    field[2][1] = 'o'

    # print('original')
    # print(field, end='\n___________________________________________________\n\n')

    print('_________________')
    for row in range(len(field)):
        print(' ', '  |  '.join(field[row]))
        print('_________________')
