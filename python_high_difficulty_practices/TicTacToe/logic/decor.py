def log(client_function):
    def wrapper(field: list, current_player: str):
        print(f'The next move is made by player - {current_player}\n'
              f'Select a number or <q> for quit to main menu..')
        return client_function(field)
    return wrapper
