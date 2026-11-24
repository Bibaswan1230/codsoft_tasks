
import math

board = [" " for _ in range(9)]

def print_board():
    print()
    for i in range(0, 9, 3):
        print(" " + " | ".join(board[i:i+3]))
        if i < 6:
            print("---+---+---")
    print()

def check_winner(player):
    wins = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]
    return any(all(board[i] == player for i in combo)
               for combo in wins)

def minimax(is_ai):
    if check_winner("O"):
        return 1
    if check_winner("X"):
        return -1
    if " " not in board:
        return 0

    if is_ai:
        best = -math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                best = max(best, minimax(False))
                board[i] = " "
        return best
    else:
        best = math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                best = min(best, minimax(True))
                board[i] = " "
        return best

def ai_move():
    best_score = -math.inf
    move = None

    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(False)
            board[i] = " "

            if score > best_score:
                best_score = score
                move = i

    if move is not None:
        board[move] = "O"

print("===== TIC TAC TOE AI =====")
print("You are X | Computer is O")
print("Enter positions from 1 to 9")

print("\nPosition guide:")
print("1 | 2 | 3")
print("--+---+--")
print("4 | 5 | 6")
print("--+---+--")
print("7 | 8 | 9")

while True:
    print_board()

    try:
        move = int(input("Enter your position (1-9): ")) - 1
    except ValueError:
        print("Please enter a valid number.")
        continue

    if move < 0 or move > 8 or board[move] != " ":
        print("Invalid position! Try again.")
        continue

    board[move] = "X"

    if check_winner("X"):
        print_board()
        print("Congratulations! You win!")
        break

    if " " not in board:
        print_board()
        print("It's a draw!")
        break

    ai_move()
    print("Computer played:")

    if check_winner("O"):
        print_board()
        print("Computer wins!")
        break

    if " " not in board:
        print_board()
        print("It's a draw!")
        break
