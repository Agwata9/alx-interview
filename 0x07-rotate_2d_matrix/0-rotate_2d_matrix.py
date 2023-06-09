#!/usr/bin/env python3
"""
an n x n 2D matrix, rotate it 90 degrees clockwise
"""


def rotate_2d_matrix(matrix):
    """
    Rotate a given n x n 2D matrix 90 degrees clockwise in-place.

    Args:
        matrix (list[list]): The input matrix to be rotated.

    Returns:
        None: The matrix is modified in-place.

    Example:
        matrix = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
        rotate_2d_matrix(matrix)
        print(matrix)
        # Output: [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
    """

    n = len(matrix)

    # Transpose the matrix
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse each row
    for i in range(n):
        matrix[i] = matrix[i][::-1]
