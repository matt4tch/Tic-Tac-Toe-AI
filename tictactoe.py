"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    x_count = 0
    o_count = 0
    for row in board:
        for pos in row:
            if pos == X:
                x_count += 1
            if pos == O:
                o_count += 1
    return X if x_count <= o_count else O



def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = set()
    length = len(board)
    for row in range(length):
        for col in range(length):
            if board[row][col] == EMPTY:
                actions.add((row, col))
    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    try:
        # check for index error
        board[action[0]][action[1]]
    except:
        raise IndexError("invalid action")
    else:
        c = copy.deepcopy(board)
        c[action[0]][action[1]] = player(board)
        return c

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    # row win check
    for row in board:
        if len(set(row)) == 1:
            if row[0] != EMPTY:
                return row[0]

    # column win check
    for col in range(len(board)):
        first = board[0][col]
        if all(first == board[i][col] for i in range(1, len(board))):
            if first != EMPTY:
                return first
    
    # diagonal win check
    first = board[0][0]
    if all(first == board[i][i] for i in range(1, len(board))):
        return first
    first = board[0][len(board)-1]
    if all(first == board[i][len(board)-1-i] for i in range(1, len(board))):
        return first
    
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if any(EMPTY in row for row in board) and winner(board) is None:
        return False
    return True

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    win = winner(board)
    if win == X:
        return 1
    if win == O:
        return -1
    return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    moves = list(actions(board))
    p = player(board)

    if p == X:
        maximum = -1000
        scores = []
        for action in moves:
            score = minvalue(result(board, action))
            maximum = max(maximum, score)
            scores.append(score)
        return moves[scores.index(maximum)]
    if p == O:
        minimum = 1000
        scores = []
        for action in moves:
            score = maxvalue(result(board, action))
            minimum = min(minimum, score)
            scores.append(score)
        return moves[scores.index(minimum)]


def minvalue(board):
    # return the minimum value of the board in its current state
    if terminal(board):
        return utility(board)
    v = 1000
    for action in actions(board):
        new = result(board, action)
        v = min(v, maxvalue(new))
    return v

def maxvalue(board):
    # return the maximum value of the board in its current state
    if terminal(board):
        return utility(board)
    v = -1000
    for action in actions(board):
        new = result(board, action)
        v = max(v, minvalue(new))
    return v
