# Author : Youssef Aitbouddroub
# gui for the tic-tac-toe human vs ai game


import tkinter as tk
from tkinter import messagebox
from Minimax import game_state, MinimaxAlphaBeta, Actions, Result, MAX, MIN , Value, Terminal

def ai_turn():
    """AI makes its move using the Minimax algorithm."""
    best_score = float('-inf')
    best_move = None
    alpha = -float('inf')
    beta = float('inf')
    maximizingPlayer = True
    for action in Actions(game_state):
        potential_game_state = Result(game_state, action, MAX)
        score = MinimaxAlphaBeta(potential_game_state, alpha, beta, maximizingPlayer)
        if score > best_score:
            best_score = score
            best_move = action
    
    if best_move:
        update_board(best_move[0], best_move[1], MAX)

def update_board(row, col, player):
    """Update the game board and check game status."""
    game_state[row][col] = player
    buttons[row][col].config(text=player, state="disabled")

    if Terminal(game_state):  # Directly use the Terminal check from Minimax
        winner = check_winner(game_state)
        end_game(winner)
    elif player == MIN:  # If it was the human's turn, let AI make its move.
        ai_turn()


def on_click(row, col):
    """Handles click events."""
    if game_state[row][col] is None:
        update_board(row, col, MIN)

def terminal(state):
    """Determines if the game has ended."""
    # Uses the Terminal function logic from the Minimax module
    return Terminal(state) 


def check_winner(state):
    """Check for a winner or a draw."""
    value = Value(state)
    if value == 1:
        return MAX
    elif value == -1:
        return MIN
    else:
        return "Draw"

def end_game(winner):
    """Handle the end of the game."""
    if winner == "Draw":
        messagebox.showinfo("Game Over", "It's a draw!")
    else:
        messagebox.showinfo("Game Over", f"{winner} wins!")
    window.destroy()

# Set up the main window
window = tk.Tk()
window.title("Tic-Tac-Toe")

# Create a 3x3 grid of buttons
buttons = [[None for _ in range(3)] for _ in range(3)]
for i in range(3):
    for j in range(3):
        button = tk.Button(window, text="", width=10, height=3,
                   command=lambda row=i, col=j: on_click(row, col),
                   font=("Helvetica", 16)) 
        button.grid(row=i, column=j)
        buttons[i][j] = button

window.mainloop()
