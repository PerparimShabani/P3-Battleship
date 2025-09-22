from random import randint

scores = {"computer": 0, "player": 0}


class Board:
    """
    Main class for the code. Sets board size, number of ships, 
    the player's name and the board type.
    Has methods for adding ships and guesses and printing the board
    """
    
    def __init__(self, size, num_ships, name, type):
        self.size = size
        self.board = [["." for x in range (size)] for y in range(size)]
        self.num_ships = num_ships
        self.name = name
        self.type = type
        self.guesses = []
        self.ships = []
        
    def print(self):
        for row in self.board: 
            print(" ".join(row))
            
    def guess(self, x, y):
        if (x, y) in self.guesses:
            return "Already guessed"
        self.guesses.append((x, y))
        self.board[x] [y] = "X"
        
        if (x, y) in self.ships:
            self.board[x] [y] = "*"
            self.ships.remove((x, y))
            return "Hit"
        else:
            return "Miss"
    
    def add_ship(self, x, y):
        if len(self.ships) >= self.num_ships:
            print("Error: you cannot add any more ships!")
        elif (x, y) in self.ships:
            pass # prevent duplicates
        else: 
            self.ships.append((x, y))
            if self.type == "player":
                self.board[x] [y] = "@"


def random_point(size):
    """
    Helper function to return a random integer between 0 and size
    """
    return randint(0, size - 1)


def valid_coordinates(x, y, board):
    """
    Check if coordinates are valid and inside the board
    """
    return 0 <= x < board.size and 0 <= y < board.size



def populate_board(board):
    """
    Randomly place ships on the board
    """
    while len(board.ships) < board.num_ships:
        x = random_point(board.size)
        y = random_point(board.size)
        board.add_ship(x, y)
        


def make_guess(board, player_type="player"):
    """
    Handles guess from the player and computer
    """
    if player_type == "player":
        while True:
            try:
                x = int(input("Enter row: "))
                y = int(input("Enter column: "))
                if valid_coordinates(x, y, board):
                    result = board.guess(x, y)
                    return result
                else:
                    print("Invalid coordinates. Try again.")
            except ValueError:
                print("Please enter numbers only.")
    else: # computer guesses randomly
        while True:
            x = random_point(board.size)
            y = random_point(board.size)
            if (x, y) not in board.guesses:
                result = board.guess(x, y)
                return result