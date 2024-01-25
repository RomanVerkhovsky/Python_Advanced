import os
import control


def view_field(field: list) -> None:
    """
    View to console game field
    :return:
    """

    # field[0][0] = 'x'
    # field[1][1] = 'o'
    # field[2][1] = 'o'

    # print('original')
    # for row in range(3):
    #     print(field[row], end='\n')

    print('_________________')
    for row in range(len(field)):
        print(' ', '  |  '.join(field[row]))
        print('_________________')


def input_user():
    input('Your move >> ')

