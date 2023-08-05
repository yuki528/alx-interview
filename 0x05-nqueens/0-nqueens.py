<<<<<<< HEAD
#!/usr/bin/python3
"""
Contains methods that find the possible solutions to the n-queens can
be placed without them attacking each other(The n-queens problem)

"""
import sys


def is_valid(board, row, col):
    """
    Checks if a position of the queen is valid

    """
    
    if 1 in board[row]:
        return False

    upper_diag = zip(range(row, -1, -1),
                     range(col, -1, -1))
    for i, j in upper_diag:
        if board[i][j] == 1:
            return False

    lower_diag = zip(range(row, len(board), 1),
                     range(col, -1, -1))
    for i, j in lower_diag:
        if board[i][j] == 1:
            return False

    return True


def nqueens_helper(board, col):
    """
    Helper function for nqueens

    """
    if col >= len(board):
        print_board(board, len(board))
    for i in range(len(board)):
        if is_valid(board, i, col):
            board[i][col] = 1
            result = nqueens_helper(board, col + 1)
            if result:
                return True
            board[i][col] = 0
    return False


def print_board(board, n):
    """
    Prints positions of the queens

    """
    b = []

    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                b.append([i, j])
    print(b)


def nqueens(n):
    """
    Finds all possible solutions to the n-queens problem

    """
    board = []
    for i in range(n):
        row = [0] * n
        board.append(row)
    nqueens_helper(board, 0)


# if __name__ == "__main__":
#     if len(sys.argv) != 2:
#         print("Usage: nqueens N")
#         exit(1)
#     queens = sys.argv[1]
#     if not queens.isnumeric():
#         print("N must be a number")
#         exit(1)
#     elif int(queens) < 4:
#         print("N must be at least 4")
#         exit(1)
#     nqueens(int(queens))
=======
#!/usr/bin/python3
"""N queens solution finder module.
"""
import sys


solutions = []
"""The list of possible solutions to the N queens problem.
"""
n = 0
"""The size of the chessboard.
"""
pos = None
"""The list of possible positions on the chessboard.
"""


def get_input():
    """Retrieves and validates this program's argument.

    Returns:
        int: The size of the chessboard.
    """
    global n
    n = 0
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except Exception:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    return n


def is_attacking(pos0, pos1):
    """Checks if the positions of two queens are in an attacking mode.

    Args:
        pos0 (list or tuple): The first queen's position.
        pos1 (list or tuple): The second queen's position.

    Returns:
        bool: True if the queens are in an attacking position else False.
    """
    if (pos0[0] == pos1[0]) or (pos0[1] == pos1[1]):
        return True
    return abs(pos0[0] - pos1[0]) == abs(pos0[1] - pos1[1])


def group_exists(group):
    """Checks if a group exists in the list of solutions.

    Args:
        group (list of integers): A group of possible positions.

    Returns:
        bool: True if it exists, otherwise False.
    """
    global solutions
    for stn in solutions:
        i = 0
        for stn_pos in stn:
            for grp_pos in group:
                if stn_pos[0] == grp_pos[0] and stn_pos[1] == grp_pos[1]:
                    i += 1
        if i == n:
            return True
    return False


def build_solution(row, group):
    """Builds a solution for the n queens problem.

    Args:
        row (int): The current row in the chessboard.
        group (list of lists of integers): The group of valid positions.
    """
    global solutions
    global n
    if row == n:
        tmp0 = group.copy()
        if not group_exists(tmp0):
            solutions.append(tmp0)
    else:
        for col in range(n):
            a = (row * n) + col
            matches = zip(list([pos[a]]) * len(group), group)
            used_positions = map(lambda x: is_attacking(x[0], x[1]), matches)
            group.append(pos[a].copy())
            if not any(used_positions):
                build_solution(row + 1, group)
            group.pop(len(group) - 1)


def get_solutions():
    """Gets the solutions for the given chessboard size.
    """
    global pos, n
    pos = list(map(lambda x: [x // n, x % n], range(n ** 2)))
    a = 0
    group = []
    build_solution(a, group)
>>>>>>> e0d5366a7954c8eeee0e1f76522f97f19a84152b
