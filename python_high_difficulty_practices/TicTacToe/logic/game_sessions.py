from python_high_difficulty_practices.TicTacToe import control
from python_high_difficulty_practices.TicTacToe.logic import game_logic


def game_pc_vs_ai():
    """
    Running pc vs ai game session
    :return:
    """
    # create game field
    field = game_logic.create_game_field()

    # create players
    current_player = 'x'
    x_player = []   # container of player 'x' moves
    o_player = []   # container of player 'o' moves
    # (0, 0), (0, 0), (1, 0), (0, 2)

    # game session loop
    is_running = True

    while is_running:
        game_logic.clear_console()
        control.AccessGUI.info_view_field(field)

        if current_player == 'x':
            select = game_logic.move_player(field, current_player)  # move of player
            game_logic.update_state_game(select, field, x_player, current_player)

            if game_logic.check_win(x_player) is True:   # checking win combo
                print('x = ', x_player)
                print(f'Gamer {x_player} WIN')
                control.AccessGUI.info_view_field(field)
                return

        else:
            select = game_logic.move_ai(field, current_player)
            game_logic.update_state_game(select, field, o_player, current_player)

            if game_logic.check_win(o_player) is True:   # checking win combo
                print('o = ', o_player)
                print(f'Gamer {current_player} WIN')
                control.AccessGUI.info_view_field(field)

                return

        is_running = not game_logic.is_end_game(field)  # checking for a draw
        current_player = game_logic.change_player(current_player)

    print('Draw')


def game_ai_vs_ai():
    """
    Running ai vs ai game session
    :return:
    """
    return
