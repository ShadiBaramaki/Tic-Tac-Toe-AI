import tkinter as tk
from tkinter import messagebox, simpledialog

# Function to display game result
def show_game_result(result):
    if result == 'Equal result':
        messagebox.showinfo("Equal result")
    else:
        messagebox.showinfo("", f"{result} won!")

# Function to evaluate the board state
def evaluate_board(board):
    score = 0

    # Function to check threats and opportunities in rows, columns, and diagonals
    def check_line(line):
        o_count = line.count('O')
        x_count = line.count('X')

        if o_count > 0 and x_count > 0:
            return 0  # If both symbols are present, no advantage for either player
        elif o_count > 0:
            return o_count
        elif x_count > 0:
            return -x_count
        return 0

    # Evaluate rows and columns
    for i in range(BOARD_SIZE):
        score += check_line([board[i][j] for j in range(BOARD_SIZE)])  # Rows
        score += check_line([board[j][i] for j in range(BOARD_SIZE)])  # Columns

    # Evaluate diagonals
    score += check_line([board[i][i] for i in range(BOARD_SIZE)])
    score += check_line([board[i][BOARD_SIZE - i - 1] for i in range(BOARD_SIZE)])

    return score

# Function to check if the game is over
def check_game_over(board):
    for i in range(BOARD_SIZE):
        if all(board[i][j] == 'X' for j in range(BOARD_SIZE)):
            return 'X'
        if all(board[i][j] == 'O' for j in range(BOARD_SIZE)):
            return 'O'

    for j in range(BOARD_SIZE):
        if all(board[i][j] == 'X' for i in range(BOARD_SIZE)):
            return 'X'
        if all(board[i][j] == 'O' for i in range(BOARD_SIZE)):
            return 'O'

    if all(board[i][i] == 'X' for i in range(BOARD_SIZE)) or all(board[i][BOARD_SIZE - i - 1] == 'X' for i in range(BOARD_SIZE)):
        return 'X'
    if all(board[i][i] == 'O' for i in range(BOARD_SIZE)) or all(board[i][BOARD_SIZE - i - 1] == 'O' for i in range(BOARD_SIZE)):
        return 'O'

    if all(board[i][j] != ' ' for i in range(BOARD_SIZE) for j in range(BOARD_SIZE)):
        return 'equal result'

    return None

# Function for player's move
def make_move(row, col):
    global player_turn, DEFAULT_DEPTH
    if board[row][col] == ' ' and player_turn:
        board[row][col] = 'X'
        buttons[row][col]['text'] = 'X'
        player_turn = False
        result = check_game_over(board)
        if result:
            show_game_result(result)
            root.quit()
        else:
            computer_turn()

# Function for AI's move
def computer_turn():
    global player_turn, DEFAULT_DEPTH
    if not any(' ' in row for row in board):
        show_game_result('equal result')
        root.quit()
        return

    move = best_move(board, depth=2)
    row, col = move
    board[row][col] = 'O'
    buttons[row][col]['text'] = 'O'
    player_turn = True
    result = check_game_over(board)
    if result:
        show_game_result(result)
        root.quit()

# Function to find the best move for the AI
def best_move(board, depth):
    best_eval = -float('inf')
    best_move = None
    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            if board[i][j] == ' ':
                board[i][j] = 'O'
                eval = alpha_beta_minimax(board, depth, -float('inf'), float('inf'), False)
                board[i][j] = ' '
                if eval > best_eval:
                    best_eval = eval
                    best_move = (i, j)
    return best_move

# Alpha-Beta Pruning with Minimax
def alpha_beta_minimax(board, depth, alpha, beta, is_maximizing):
    result = check_game_over(board)
    if result:
        if result == 'Equal result':
            return 0
        elif result == 'X':
            return -1000
        else:
            return 1000

    if depth == 0:
        return evaluate_board(board)

    if is_maximizing:
        max_eval = -float('inf')
        for i in range(BOARD_SIZE):
            for j in range(BOARD_SIZE):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    eval = alpha_beta_minimax(board, depth - 1, alpha, beta, False)
                    board[i][j] = ' '
                    max_eval = max(max_eval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = float('inf')
        for i in range(BOARD_SIZE):
            for j in range(BOARD_SIZE):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    eval = alpha_beta_minimax(board, depth - 1, alpha, beta, True)
                    board[i][j] = ' '
                    min_eval = min(min_eval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
            if beta <= alpha:
                break
        return min_eval

# Main function to start the game
def main():
    global player_turn, board, buttons, root, BOARD_SIZE, MAX_DEPTH

    BOARD_SIZE = simpledialog.askinteger("Board Size", "Please enter board size:")
    if BOARD_SIZE is None:
        return

    difficulty_level = simpledialog.askstring("Level", "Select difficulty (hard/easy)")
    if difficulty_level is None:
        return

if __name__ == "__main__":
    main()

    root = tk.Tk()
    root.title("Tic Tac Toe")

    board = [[' ' for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
    player_turn = True

    buttons = [[tk.Button(root, text='', font=('Helvetica', 20), height=2, width=5,
                          command=lambda row=row, col=col: make_move(row, col))
               for col in range(BOARD_SIZE)] for row in range(BOARD_SIZE)]

    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            buttons[i][j].grid(row=i, column=j)

    root.mainloop()
