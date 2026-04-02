def is_consistent(board, row, col, value):
    # Row check
    for c in range(9):
        if board[row][c] == value:
            return False

    # Column check
    for r in range(9):
        if board[r][col] == value:
            return False

    # 3x3 Box check
    start_r, start_c = 3 * (row // 3), 3 * (col // 3)
    for r in range(start_r, start_r + 3):
        for c in range(start_c, start_c + 3):
            if board[r][c] == value:
                return False

    return True


def select_unassigned_variable(board):
    for r in range(9):
        for c in range(9):
            if board[r][c] == 0:
                return r, c
    return None


def backtrack(board):
    pos = select_unassigned_variable(board)

    if pos is None:
        return True

    row, col = pos

    for value in range(1, 10):
        if is_consistent(board, row, col, value):
            board[row][col] = value

            if backtrack(board):
                return True

            board[row][col] = 0

    return False


# Example Sudoku (0 = empty)
board = [
    [5,3,0,0,7,0,0,0,0],
    [6,0,0,1,9,5,0,0,0],
    [0,9,8,0,0,0,0,6,0],
    [8,0,0,0,6,0,0,0,3],
    [4,0,0,8,0,3,0,0,1],
    [7,0,0,0,2,0,0,0,6],
    [0,6,0,0,0,0,2,8,0],
    [0,0,0,4,1,9,0,0,5],
    [0,0,0,0,8,0,0,7,9]
]

backtrack(board)

print("Solved Sudoku:\n")
for row in board:
    print(row)
