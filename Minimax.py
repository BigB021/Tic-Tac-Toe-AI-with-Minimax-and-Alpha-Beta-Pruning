# Author : Youssef Aitbouddroub
# Minimax and Alpha-Beta Pruning for Tic-Tac-Toe

# This Python script implements the Minimax algorithm with Alpha-Beta pruning optimized for a Tic-Tac-Toe game.
# It demonstrates a simple artificial intelligence (AI) that can play Tic-Tac-Toe by evaluating game states,
# predicting opponent moves, and making optimal decisions.

# Constants
MAX = 'X'  # Represents the AI player using 'X'
MIN = 'O'  # Represents the human player using 'O'

# Global variable representing the initial state of the game board.
# None indicates an empty cell.
game_state = [
    [None, None, None],
    [None, None, None],
    [None, None, None]
]

# Functions

def MinimaxAlphaBeta(game_state, alpha, beta, maximizingPlayer):
    """
    Implements the Minimax algorithm with Alpha-Beta pruning.
    
    Args:
        game_state: Current state of the game board as a 2D list.
        alpha: Alpha value for pruning, initially negative infinity.
        beta: Beta value for pruning, initially positive infinity.
        maximizingPlayer: Boolean indicating if the current player is maximizing or minimizing.

    Returns:
        The score of the current game state.
    """
    if Terminal(game_state):
        return Value(game_state)
    
    if maximizingPlayer:
        return MaxValue(game_state, alpha, beta)
    else:
        return MinValue(game_state, alpha, beta)

def Terminal(game_state):
    """
    Checks if the game has reached a terminal state (win, lose, or draw).

    Args:
        game_state: The current state of the game board.

    Returns:
        True if the game is over, False otherwise.
    """
    # Check for win in rows, columns, and diagonals
    for i in range(3):
        if game_state[i][0] == game_state[i][1] == game_state[i][2] != None or \
           game_state[0][i] == game_state[1][i] == game_state[2][i] != None:
            return True
    if game_state[0][0] == game_state[1][1] == game_state[2][2] != None or \
       game_state[2][0] == game_state[1][1] == game_state[0][2] != None:
        return True

    # Check for draw (no empty cells left)
    for row in game_state:
        if None in row:
            return False  
    return True 

def Actions(game_state):
    """
    Generates all possible actions (moves) available in the current game state.

    Args:
        game_state: The current state of the game board.

    Returns:
        A list of tuples representing possible moves (i, j), where i is the row and j is the column.
    """
    actions = []
    for i in range(3):
        for j in range(3):
            if game_state[i][j] == None:
                actions.append((i, j))
    return actions

def Result(game_state, action, move):
    """
    Generates a new game state by applying a move to the current game state.

    Args:
        game_state: The current state of the game board.
        action: The action to be applied, represented as a tuple (i, j).
        move: The player making the move, either MAX or MIN.

    Returns:
        A new game state after applying the move.
    """
    new_state = [row[:] for row in game_state]  # Deep copy of the game state
    row, column = action
    new_state[row][column] = move
    return new_state

def MaxValue(game_state, alpha, beta):
    """
    Evaluates the maximum score that the maximizing player can achieve from the current game state.

    Args:
        game_state: The current state of the game board.
        alpha: The current alpha value.
        beta: The current beta value.

    Returns:
        The maximum score achievable.
    """
    if Terminal(game_state):
        return Value(game_state)
    
    value = -float('inf')
    for action in Actions(game_state):
        value = max(value, MinimaxAlphaBeta(Result(game_state, action, MAX), alpha, beta, False))
        if value >= beta:  # Beta cut-off
            break
        alpha = max(alpha, value)
    return value

def MinValue(game_state, alpha, beta):
    """
    Evaluates the minimum score that the minimizing player can achieve from the current game state.

    Args:
        game_state: The current state of the game board.
        alpha: The current alpha value.
        beta: The current beta value.

    Returns:
        The minimum score achievable.
    """
    if Terminal(game_state):
        return Value(game_state)
    
    value = float('inf')
    for action in Actions(game_state):
        value = min(value, MinimaxAlphaBeta(Result(game_state, action, MIN), alpha, beta, True))
        if value <= alpha:  # Alpha cut-off
            break
        beta = min(beta, value)
    return value

def Value(game_state):
    """
    Evaluates the score of the current game state.

    Args:
        game_state: The current state of the game board.

    Returns:
        1 if MAX wins, -1 if MIN wins, 0 for a draw, and None if the game is ongoing.
    """
    # Check for wins
    for i in range(3):
        if game_state[i][0] == game_state[i][1] == game_state[i][2] == 'X' or \
           game_state[0][i] == game_state[1][i] == game_state[2][i] == 'X':
            return 1
        elif game_state[i][0] == game_state[i][1] == game_state[i][2] == 'O' or \
             game_state[0][i] == game_state[1][i] == game_state[2][i] == 'O':
            return -1
    if game_state[0][0] == game_state[1][1] == game_state[2][2] == 'X' or \
       game_state[2][0] == game_state[1][1] == game_state[0][2] == 'X':
        return 1
    elif game_state[0][0] == game_state[1][1] == game_state[2][2] == 'O' or \
         game_state[2][0] == game_state[1][1] == game_state[0][2] == 'O':
        return -1
    
    # Check for draw
    if all(None not in row for row in game_state):
        return 0
    return None


