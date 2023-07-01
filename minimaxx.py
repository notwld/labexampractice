import random

def print_board(board):
    """
    Prints the Tic-Tac-Toe board.
    """
    print("---------")
    for row in board:
        print("|", end="")
        for cell in row:
            print(cell, end="|")
        print("\n---------")

def is_full(board):
    """
    Checks if the board is full.
    """
    for row in board:
        for cell in row:
            if cell == "-":
                return False
    return True

def get_winner(board):
    """
    Determines the winner of the game.
    Returns 'X' if X wins, 'O' if O wins, or '-' if there is no winner yet.
    """
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] != "-":
            return row[0]

    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != "-":
            return board[0][col]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != "-":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != "-":
        return board[0][2]

    return "-"

def get_empty_cells(board):
    """
    Returns a list of empty cells on the board.
    """
    empty_cells = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == "-":
                empty_cells.append((i, j))
    return empty_cells

def evaluate(board):
    """
    Evaluates the current state of the board.
    Returns +1 if X wins, -1 if O wins, or 0 for a tie.
    """
    winner = get_winner(board)
    if winner == "X":
        return 1
    elif winner == "O":
        return -1
    else:
        return 0

def minimax(board, depth, is_maximizing):
    """
    Minimax algorithm implementation.
    """
    if get_winner(board) != "-":
        return evaluate(board)

    if is_full(board):
        return 0

    if is_maximizing:
        best_score = float("-inf")
        for cell in get_empty_cells(board):
            i, j = cell
            board[i][j] = "X"
            score = minimax(board, depth + 1, False)
            board[i][j] = "-"
            best_score = max(score, best_score)
        return best_score

    else:
        best_score = float("inf")
        for cell in get_empty_cells(board):
            i, j = cell
            board[i][j] = "O"
            score = minimax(board, depth + 1, True)
            board[i][j] = "-"
            best_score = min(score, best_score)
        return best_score

def get_best_move(board):
    """
    Finds the best move for the AI using the Minimax algorithm.
    """
    best_score = float("-inf")
    best_move = None
    for cell in get_empty_cells(board):
        i, j = cell
        board[i][j] = "X"
        score = minimax(board, 0, False)
        board[i][j] = "-"
        if score > best_score:
            best_score = score
            best_move = cell
    return best_move

def play_game():
    """
    Plays a simplified Tic-Tac-Toe game against the AI.
    """
    board = [["-" for _ in range(3)] for _ in range(3)]
    print("Welcome to Simplified Tic-Tac-Toe!")
    print_board(board)

    while True:
        # Player's turn
        position = int(input("Enter the position on the board (1-9): "))
        row = (position - 1) // 3
        col = (position - 1) % 3
        if board[row][col] == "-":
            board[row][col] = "O"
        else:
            print("Invalid move! Try again.")
            continue

        # Check for game over
        winner = get_winner(board)
        if winner == "O":
            print("Congratulations! You won!")
            break
        elif is_full(board):
            print("It's a tie!")
            break

        # AI's turn
        print("AI is thinking...")
        ai_move = get_best_move(board)
        board[ai_move[0]][ai_move[1]] = "X"

        # Check for game over
        winner = get_winner(board)
        if winner == "X":
            print("AI wins!")
            break
        elif is_full(board):
            print("It's a tie!")
            break

        print_board(board)

play_game()
