import random


def print_board(game_board: [[int, ], ]) -> None:
    """
    Print a formatted version of the game board.
    :param game_board: a 4x4 2D list of integers representing a game of 2048
    """
    print()
    for row in game_board:
        print("+----+" * 4)
        print(''.join(f"|{cell if cell else '':^4}|" for cell in row))
        print("+----+" * 4)
    
    print('Debug: The board is', game_board)
    print()


def place_random(game_board: [[int, ], ]) -> {str: int, }:
    """
    Generates a random value and coordinates for the next number to be placed on the board.
    Will raise error if the provided board is full.
    :param game_board: a 4x4 2D list of integers representing a game of 2048
    :return: dictionary with the following keys: {'row': int, 'column': int, 'value': int}
    """
    empty_cells = [(y, x) for y, row in enumerate(game_board) for x, cell in enumerate(row) if not cell]
    if not empty_cells:
        raise Exception("Board Full")
    return dict(
        zip(('row', 'column', 'value'), (*random.choice(empty_cells), (2 if random.random() * 100 < 90 else 4))))