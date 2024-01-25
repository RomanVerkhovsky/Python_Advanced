def log(client_function):
    def wrapper(current_player: str):
        print(f'The next move is made by player - {current_player}\n'
              f'Select an empty cell >>')
        return client_function()
    return wrapper


# def move_request(client_function):
#     def wrapper(current_player: str):
#         print(f'')
