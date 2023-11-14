def create_board():
    """
    Creates a board to be used in 2 seperate functions one to be used to make the player a board
    and another to be used to make the computer a board.
    """
    print('   0 1 2 3 4 5 6 7 8 9')
    for x in range(10):
        row = [f'{x} ']
        for y in range(10):
            empty_space =  '-'
            row.append(empty_space)
        print(' '.join(row))

create_board()