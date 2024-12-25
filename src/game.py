class Game:
    def __init__(self):
        self.board = [' ' for _ in range(9)]  # A list to hold the board state
        self.current_player = 'X'  # Starting player

    def start_game(self):
        self.board = [' ' for _ in range(9)]
        self.current_player = 'X'

    def check_winner(self):
        winning_combinations = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Horizontal
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Vertical
            (0, 4, 8), (2, 4, 6)               # Diagonal
        ]
        for combo in winning_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != ' ':
                return self.board[combo[0]]  # Return the winner ('X' or 'O')
        if ' ' not in self.board:
            return 'Draw'  # Return 'Draw' if the board is full
        return None  # No winner yet

    def reset_game(self):
        self.start_game()  # Reset the game to the initial state