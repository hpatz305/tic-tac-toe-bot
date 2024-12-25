import random


class TicTacToeBot:
    def __init__(self, player_symbol):
        self.player_symbol = player_symbol
        self.opponent_symbol = 'O' if player_symbol == 'X' else 'X'

    def make_move(self, board):
        # Check for a winning move
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = self.player_symbol
                    if self.check_winner(board, self.player_symbol):
                        return (i, j)
                    board[i][j] = ' '

        # Block opponent's winning move
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = self.opponent_symbol
                    if self.check_winner(board, self.opponent_symbol):
                        board[i][j] = self.player_symbol
                        return (i, j)
                    board[i][j] = ' '

        # Choose a random move
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    return (i, j)

    def check_winner(self, board, player):
        win_conditions = [
            [board[0][0], board[0][1], board[0][2]],
            [board[1][0], board[1][1], board[1][2]],
            [board[2][0], board[2][1], board[2][2]],
            [board[0][0], board[1][0], board[2][0]],
            [board[0][1], board[1][1], board[2][1]],
            [board[0][2], board[1][2], board[2][2]],
            [board[0][0], board[1][1], board[2][2]],
            [board[2][0], board[1][1], board[0][2]],
        ]
        return [player, player, player] in win_conditions


def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)


def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    user_symbol = ""
    while user_symbol not in ["X", "O"]:
        user_symbol = input("Do you want to be X or O? ").upper()
        if user_symbol not in ["X", "O"]:
            print("Invalid choice. Please choose X or O.")
    
    bot = TicTacToeBot("O" if user_symbol == "X" else "X")
    current_player = user_symbol

    print("Welcome to Tic Tac Toe!")
    print_board(board)

    while True:
        if current_player == user_symbol:
            while True:
                try:
                    row = int(input("Enter the row (0, 1, 2): "))
                    col = int(input("Enter the column (0, 1, 2): "))
                    if row in [0, 1, 2] and col in [0, 1, 2] and board[row][col] == " ":
                        break
                    else:
                        print("Invalid move. Try again.")
                except ValueError:
                    print("Invalid input. Please enter numbers 0, 1, or 2.")
        else:
            row, col = bot.make_move(board)
            print(f"Bot chose: {row}, {col}")

        board[row][col] = current_player
        print_board(board)

        if bot.check_winner(board, current_player):
            print(f"Player {current_player} wins!")
            break

        if not any(" " in row for row in board):
            print("It's a tie!")
            break

        current_player = "O" if current_player == "X" else "X"


if __name__ == "__main__":
    main()