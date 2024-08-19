#!/usr/bin/python3
"""
Rotate 2D Matrix
This module contains a function to rotate an n x n 2D matrix 90 degrees clockwise in-place.
"""

def rotate_2d_matrix(matrix):
    """
    Rotate a two-dimensional n x n matrix 90 degrees clockwise.

    Args:
        matrix (list[list[int]]): A 2D list (matrix) representing the matrix to be rotated. 
                                  Each element is an integer, and the matrix is n x n.

    Returns:
        None: The matrix is rotated in-place, and the function does not return any value.

    Example:
        >>> matrix = [
        >>>     [1, 2, 3],
        >>>     [4, 5, 6],
        >>>     [7, 8, 9]
        >>> ]
        >>> rotate_2d_matrix(matrix)
        >>> print(matrix)
        >>> [
        >>>     [7, 4, 1],
        >>>     [8, 5, 2],
        >>>     [9, 6, 3]
        >>> ]

    Description:
        The function performs an in-place rotation of the given n x n matrix by 90 degrees clockwise.
        It does this by performing a series of element swaps:
        1. Top element with left element
        2. Left element with bottom element
        3. Bottom element with right element
        4. Right element with the original top element

        The process is repeated layer by layer from the outermost layer to the innermost layer.
    """
    n = len(matrix)
    for i in range(int(n / 2)):
        y = (n - i - 1)
        for j in range(i, y):
            x = (n - 1 - j)
            # Current number
            tmp = matrix[i][j]
            # Change top for left
            matrix[i][j] = matrix[x][i]
            # Change left for bottom
            matrix[x][i] = matrix[y][x]
            # Change bottom for right
            matrix[y][x] = matrix[j][y]
            # Change right for top
            matrix[j][y] = tmp

