# Battle Ships

Battle Ships is a Python terminal game, which runs on Code Institute's mock terminal on Heroku.

Players can try and beat the computer by finding all 10 of the computer's battleships before the computer finds all 10 of the player's ships. Each ship takes up one square of the board.

[You can find the live version of my project here.](https://battle-ships-python-game-9b5b78971714.herokuapp.com/)

![pythonprjct](https://github.com/benbarker04/battle-ships/assets/131170958/c35eb5bc-da9a-4055-a72e-559b95a2927e)

## How to play

Battle Ships is based on the board game of the same name. You can read more about it on [wikipedia](https://en.wikipedia.org/wiki/Battleship_(game)).

In this version of the classic game, the player will enter their name into the terminal and two boards will be generated and their ships will be randomly placed across the boards.

The player can see where their ships are which are indicated on the board by a `0`, but will not be able to see where the computer's are.

Guesses are marked on the boards with an `X` if they are incorrect and are marked with a `#` if they are correct.

The player and the computer will take turns to try and guess and sink each other's battleships.

The first one to sink all of the opponent's ships is the winner.

## Existing Features

- Random board generation
  - Ships are randomly placed on both the player's and the computer's boards.
  - The player cannot see where the computer's ships are.

![randomboardgen](https://github.com/benbarker04/battle-ships/assets/131170958/53cf96af-31ed-4a91-a4be-b78e5fbc6548)

- Play against the computer.
- Accepts user input.

![inputboard](https://github.com/benbarker04/battle-ships/assets/131170958/acd82d19-f855-4ba1-be45-79836c48d5b5)

- Input validation and error-checking.
   - You cannot enter coordinates outside the size of the grid.
   - You must enter numbers.
   - You cannot enter the same guess twice.

![invalidinput](https://github.com/benbarker04/battle-ships/assets/131170958/0d53b3c4-0af0-4d9f-a6ca-aa906f46bc55)

- Data maintained in class instances.

## Future Features

- Allow the player to select the board size and the number of ships.
- Allow the player to choose where their ships go.
- Have ships that are larger than 1x1.
- Have a score counter.

## Data Model

I have decided to use a Board class as my model. The game creates two instances of the Board class to hold the player's and the computer's board.

The Board class stores the board size, the number of ships, the position of the ships, guesses against the board, and details such as the board type (player's board or the computer's) and the player's name.

The class also has methods to play the game, such as `print_board` method to print out the current board and a `place_ships` method to place the ships onto the board.

## Testing

I have manually tested the project by doing the following:
- Passed the code through the PEP8 linter.
- Given invalid inputs: strings when numbers were expected, out-of-bounds inputs, same input twice.
- Tested in the code terminal and the Code Institue Heroku terminal.

### Bugs

- When I deployed my project to Code Institute's mock terminal for Heroku I found no bugs.

### Validator Testing

- PEP8
   - The only issue I had and is still left unresolved is when I passed my code through the PEP8 linter it came back saying some of my lines were to long, i spent a while trying to resolve this issue but found no solution if i had more time i would like to figure out how to solve this issue.

## Deployment

This project was deployed using Code Institute's mock terminal for Heroku by doing the following:

- Fork or clone this repository.
- Create a new Heroku app.
- Set the buildbacks to `Python` and `NodeJS` in that order.
- Link the Heroku app to the repository.
- Click on **Deploy**.
