def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def is_valid_move(board, row, col):
    return 0 <= row < 3 and 0 <= col < 3 and board[row][col] == " "