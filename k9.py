import numpy as np


board = np.array([
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
])


def is_valid(board, row, col, num):
    if num in board[row, :] or num in board[:, col]:
        return False


    start_row, start_col = (row // 3) * 3, (col // 3) * 3
    if num in board[start_row:start_row+3, start_col:start_col+3]:
        return False

    return True


def solve_sudoku(board):
    empty = np.argwhere(board == 0)
    if len(empty) == 0:
        return True

    row, col = empty[0]

    for num in range(1, 10):
        if is_valid(board, row, col, num):
            board[row, col] = num  
            if solve_sudoku(board):
                return True
            
            board[row, col] = 0
    
    return False


if solve_sudoku(board):
    print("Solved Sudoku:\n", board)
else:
    print("No solution exists.")
