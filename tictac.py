import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def is_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_draw(board):
    return all(cell != ' ' for row in board for cell in row)

def get_empty_cells(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']

def minimax(board, depth, maximizing_player):
    if is_winner(board, 'O'):
        return 1
    if is_winner(board, 'X'):
        return -1
    if is_draw(board):
        return 0

    if maximizing_player:
        max_eval = -float('inf')
        for i, j in get_empty_cells(board):
            board[i][j] = 'O'
            eval = minimax(board, depth + 1, False)
            board[i][j] = ' '
            max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('inf')
        for i, j in get_empty_cells(board):
            board[i][j] = 'X'
            eval = minimax(board, depth + 1, True)
            board[i][j] = ' '
            min_eval = min(min_eval, eval)
        return min_eval

def best_move(board):
    best_eval = -float('inf')
    best_move = None

    for i, j in get_empty_cells(board):
        board[i][j] = 'O'
        eval = minimax(board, 0, False)
        board[i][j] = ' '

        if eval > best_eval:
            best_eval = eval
            best_move = (i, j)

    return best_move

def play_game():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    player = 'X'

    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    while True:
        if player == 'X':
            row, col = map(int, input("Enter your move (row [0-2] and column [0-2]): ").split())
            if board[row][col] != ' ':
                print("Invalid move. Try again.")
                continue
        else:
            print("AI's turn:")
            row, col = best_move(board)

        board[row][col] = player
        print_board(board)

        if is_winner(board, player):
            print(f"{player} wins!")
            break
        elif is_draw(board):
            print("It's a draw!")
            break

        player = 'X' if player == 'O' else 'O'

if __name__ == "__main__":
    play_game()
