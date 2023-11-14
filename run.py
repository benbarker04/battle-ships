import random

class Board:
    def create_board(self):
        """
        Creates an empty board.
        """
        return [['.'] * self.size for _ in range(self.size)]

    def __init__(self, name = None):
        self.size = 10
        self.empty_space = '.'
        self.ship_symbol = '0'
        self.name = name
        self.board = self.create_board()

    def print_board(self):
        """
        Prints the board with column labels.
        """
        print('   0 1 2 3 4 5 6 7 8 9')
        for i, row in enumerate(self.board):
            print(f'{i}  {" ".join(row)}')
        if self.name:
            print(f'\n{self.name}\'s Board')

    def place_ships(self, num_ships):
        """
        Randomly places the specified number of ships on the board.
        """
        for _ in range(num_ships):
            row = random.randint(0, self.size - 1)
            col = random.randint(0, self.size - 1)
            while self.board[row][col] == self.ship_symbol:
                row = random.randint(0, self.size - 1)
                col = random.randint(0, self.size - 1)
            self.board[row][col] = self.ship_symbol

def new_game():
    """
    Starts a new game and prints everything needed on the console.
    """
    print('Welcome to Battle Ships!')
    print("First to destroy all of the other player's ships wins.\n")
    player_name = input('Enter your name: ')
    print()

    player_board = Board(name = player_name)
    bot_board = Board(name = "Bot")

    player_board.place_ships(num_ships = 10)
    bot_board.place_ships(num_ships = 10)

    player_board.print_board()
    bot_board.print_board()

new_game()
