from python_high_difficulty_practices.TicTacToe import control
from python_high_difficulty_practices.TicTacToe.logic import game_logic


async def game_pc_vs_ai() -> None:
    """
    Running pc vs ai game session
    :return:
    """
    # create game field
    field = game_logic.create_game_field()

    # create players
    x_player = []   # container of player 'x' moves
    o_player = []   # container of player 'o' moves

    current_player = 'x'

    # game session loop
    is_running = True

    while is_running:

        game_logic.clear_console()
        control.AccessGUI.info_view_field(field)

        if current_player == 'x':
            select = await game_logic.move_player(field, current_player)    # move of player

        else:
            select = await game_logic.move_ai(field, current_player)    # move of AI

        if select == 'q':
            return

        # update game field and container of player after moving
        game_logic.update_state_game(select, field, game_logic.current_player_container(current_player, x_player,
                                                                                        o_player), current_player)

        # checking win combo in container
        if game_logic.check_win(game_logic.current_player_container(current_player, x_player, o_player)) is True:
            control.AccessGUI.info_view_field(field)
            control.AccessGUI.info_win(current_player)
            control.AccessGUI.input_user()
            return

        # checking for a draw
        is_running = not game_logic.is_end_game(field)

        # change current player before next moving
        current_player = game_logic.change_player(current_player)

    control.AccessGUI.info_draw()
    control.AccessGUI.input_user()


async def game_pc_vs_pc() -> None:
    """
        Running pc vs pc game session
        :return:
        """
    # create game field
    field = game_logic.create_game_field()

    # create players
    x_player = []  # container of player 'x' moves
    o_player = []  # container of player 'o' moves

    current_player = 'x'

    # game session loop
    is_running = True

    while is_running:

        game_logic.clear_console()
        control.AccessGUI.info_view_field(field)

        if current_player == 'x':
            select = await game_logic.move_player(field, current_player)  # move of player 1

        else:
            select = await game_logic.move_player(field, current_player)  # move of player 2

        if select == 'q':
            return

        # update game field and container of player after moving
        game_logic.update_state_game(select, field, game_logic.current_player_container(current_player, x_player,
                                                                                        o_player), current_player)

        # checking win combo in container
        if game_logic.check_win(game_logic.current_player_container(current_player, x_player, o_player)) is True:
            control.AccessGUI.info_view_field(field)
            control.AccessGUI.info_win(current_player)
            control.AccessGUI.input_user()
            return

        # checking for a draw
        is_running = not game_logic.is_end_game(field)

        # change current player before next moving
        current_player = game_logic.change_player(current_player)

    control.AccessGUI.info_draw()
    control.AccessGUI.input_user()


async def game_ai_vs_ai() -> None:
    """
    Running ai vs ai game session
    :return:
    """
    # create game field
    field = game_logic.create_game_field()

    # create players
    x_player = []  # container of player 'x' moves
    o_player = []  # container of player 'o' moves

    current_player = 'x'

    # game session loop
    is_running = True

    while is_running:

        game_logic.clear_console()
        control.AccessGUI.info_view_field(field)

        # move of AI
        select = await game_logic.move_ai(field, current_player)

        # update game field and container of player after moving
        game_logic.update_state_game(select, field, game_logic.current_player_container(current_player, x_player,
                                                                                        o_player), current_player)

        # checking win combo in container
        if game_logic.check_win(game_logic.current_player_container(current_player, x_player, o_player)) is True:
            control.AccessGUI.info_view_field(field)
            control.AccessGUI.info_win(current_player)
            control.AccessGUI.input_user()
            return

        # checking for a draw
        is_running = not game_logic.is_end_game(field)

        # change current player before next moving
        current_player = game_logic.change_player(current_player)

    control.AccessGUI.info_draw()
    control.AccessGUI.input_user()
