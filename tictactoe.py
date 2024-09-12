import math
import random
PLAYER_X = 'X'
PLAYER_O = 'O'
EMPTY = ' '
def print_board(board):
    for i in range(3):
        print(f"{board[i*3]} | {board[i*3+1]} | {board[i*3+2]}")
        if i < 2:
            print("---------")

def is_board_full(board):
    return all(cell != EMPTY for cell in board)
def check_winner(board):
    winning_combinations = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8), 
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  
        (0, 4, 8), (2, 4, 6)              
    ]
    
    for a, b, c in winning_combinations:
        if board[a] == board[b] == board[c] and board[a] != EMPTY:
            return board[a]
    
    return None
def minimax(board, depth, is_maximizing, alpha, beta):
    winner = check_winner(board)
    if winner == PLAYER_X:
        return 10 - depth
    elif winner == PLAYER_O:
        return depth - 10
    elif is_board_full(board):
        return 0
    
    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if board[i] == EMPTY:
                board[i] = PLAYER_X
                score = minimax(board, depth + 1, False, alpha, beta)
                board[i] = EMPTY
                best_score = max(score, best_score)
                alpha = max(alpha, score)
                if beta <= alpha:
                    break
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if board[i] == EMPTY:
                board[i] = PLAYER_O
                score = minimax(board, depth + 1, True, alpha, beta)
                board[i] = EMPTY
                best_score = min(score, best_score)
                beta = min(beta, score)
                if beta <= alpha:
                    break
        return best_score
def find_best_move(board):
    best_score = -math.inf
    best_move = None
    
    for i in range(9):
        if board[i] == EMPTY:
            board[i] = PLAYER_X
            score = minimax(board, 0, False, -math.inf, math.inf)
            board[i] = EMPTY
            if score > best_score:
                best_score = score
                best_move = i
    
    return best_move

# Main function to play the game
def play_game():
    board = [EMPTY] * 9
    current_player = PLAYER_X
    
    while True:
        print_board(board)
        
        if current_player == PLAYER_X:
            print("AI's turn!")
            move = find_best_move(board)
        else:
            move = int(input("Enter your move (0-8): "))
        
        if board[move] == EMPTY:
            board[move] = current_player
        else:
            print("Invalid move, try again.")
            continue
        
        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f"Player {winner} wins!")
            break
        
        if is_board_full(board):
            print_board(board)
            print("It's a draw!")
            break
        
        current_player = PLAYER_X if current_player == PLAYER_O else PLAYER_O

if __name__ == "__main__":
    play_game()
