def log(client_function):
    def wrapper(field: list, current_player: str):
        print(f'The next move is made by player - {current_player}')
        return client_function(field)
    return wrapper
