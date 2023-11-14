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

    def print_board(self, hidden=False):
        """
        Prints the board with column labels.
        If hidden is True, ship positions are hidden.
        """
        if self.name:
            print(f"{self.name}'s Board")
        else:
            print("Bot's board")

        print('   0 1 2 3 4 5 6 7 8 9')
        for i, row in enumerate(self.board):
            print(f'{i}  {" ".join([self.empty_space if hidden and cell == self.ship_symbol else cell for cell in row])}')

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

def player_choice(board):
    """
    Takes player input for row and column on the bot's board and updates the board.
    """
    while True:
        try:
            row = int(input('Enter the row (0 - 9): '))
            col = int(input('Enter the column (0 - 9): '))
            if 0 <= row < board.size and 0 <= col < board.size:
                if board.board[row][col] == board.ship_symbol:
                    print('Hit!')
                    board.board[row][col] = 'H'
                else:
                    print('Miss!')
                    board.board[row][col] = 'M'
                break
            else:
                print('Invalid input. Row and column must be between 0 and 9.')
        except ValueError:
            print('Invalid input. Please enter a number.')

def bot_choice(board):
    """
    Simulates the bot's move on the player's board by choosing random row and column coordinates.
    """
    while True:
        row = random.randint(0, board.size - 1)
        col = random.randint(0, board.size - 1)
        if board.board[row][col] == board.ship_symbol:
            print('Bot hit your ship!')
            board.board[row][col] = 'H'
        else:
            print('Bot missed!')
            board.board[row][col] = 'M'
        break

def new_game():
    """
    Starts a new game and prints everything needed on the console.
    """
    print('Welcome to Battle Ships!')
    print('Rules')
    print("First to destroy all 10 of the other player's ships wins.")
    print("When a ship has been hit a 'H' will appear in the position")
    print("if nothing has been hit a 'M' will appear in that position\n")
    player_name = input('Enter your name: ')
    print()

    player_board = Board(name = player_name)
    bot_board = Board(name = "Bot")

    player_board.place_ships(num_ships = 10)
    bot_board.place_ships(num_ships = 10)

    player_board.print_board()
    bot_board.print_board(hidden=True)

    player_choice(bot_board)

    bot_choice(player_board)

    print(f"\n{player_name}'s Updated Board")
    player_board.print_board()
    print('\nBot\'s Updated Board')
    bot_board.print_board(hidden=True)

new_game()
