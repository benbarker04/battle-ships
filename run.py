def create_board():
    """
    Creates a board to be used in 2 seperate functions one to be used to make the player a board
    and another to be used to make the computer a board.
    """
    print('   0 1 2 3 4 5 6 7 8 9')
    for x in range(10):
        row = [f'{x} ']
        for y in range(10):
            empty_space =  '.'
            row.append(empty_space)
        print(' '.join(row))

def create_player_board(name):
    """
    Creates board for the player.
    """
    print(f"      {name}'s board")
    create_board()

def create_bot_board():
    """
    Creates board for the computer.
    """
    print("       Bot's board")
    create_board()

def new_game():
    """
    starts a new game and prints everything needed on to the console
    """
    print('Welcome to Battle Ships!')
    print("First to destroy all of the other player's ships wins.\n")
    name = input('Enter your name:')
    print('\n')
    create_player_board(name)
    create_bot_board()

new_game()