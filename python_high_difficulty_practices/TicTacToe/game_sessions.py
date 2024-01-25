import control
import game_logic


def game_pc_and_ai():
    """

    :return:
    """
    # create game field
    field = game_logic.create_game_field()

    # create players
    current_player = 'x'
    x_player = []
    o_player = []

    # game session loop
    is_running = True

    while is_running:
        control.AccessGUI.view_field(field)
        if current_player == 'x':
            game_logic.move_player(current_player)
            break

        else:
            game_logic.move_ai(current_player)


def game_ai_and_ai():
    pass
