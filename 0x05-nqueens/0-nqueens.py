#!/usr/bin/env python3

import sys

def is_safe(board, row, col):
    # Check if there is a queen in the same column
    for i in range(row):
        if board[i][col] == 'Q':
            return False

    # Check if there is a queen in the upper left diagonal
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j -= 1

    # Check if there is a queen in the upper right diagonal
    i, j = row, col
    while i >= 0 and j < len(board):
        if board[i][j] == 'Q':
            return False
        i -= 1
        j += 1

    return True

def solve_nqueens(n):
    board = [['.' for _ in range(n)] for _ in range(n)]
    solutions = []
    backtrack(board, 0, solutions)
    return solutions

def backtrack(board, row, solutions):
    if row == len(board):
        # Found a valid solution, convert the board to a solution string
        solution = [''.join(row) for row in board]
        solutions.append(solution)
        return

    for col in range(len(board)):
        if is_safe(board, row, col):
            # Place a queen and proceed to the next row
            board[row][col] = 'Q'
            backtrack(board, row + 1, solutions)
            # Remove the queen for backtracking
            board[row][col] = '.'

def print_solutions(solutions):
    for solution in solutions:
        for row in solution:
            print(row)
        print()

def main():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = solve_nqueens(n)
    print_solutions(solutions)

if __name__ == '__main__':
    main()

