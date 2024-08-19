Array Operations in Python
This repository contains examples and implementations of various operations on 1D and 2D arrays in Python. It demonstrates how to rotate 2D matrices and perform basic operations on 1D arrays.

1D Array Operations
1. Basic Operations
You can perform various operations on 1D arrays (lists in Python), including:

Traversal: Accessing each element in the array.
Modification: Changing the value of specific elements.
Aggregation: Calculating sums, averages, or other aggregate values.
Example:

python
Copy code
# Initialize a 1D array
array = [1, 2, 3, 4, 5]

# Accessing elements
print(array[0])  # Output: 1

# Modifying elements
array[1] = 10
print(array)  # Output: [1, 10, 3, 4, 5]

# Aggregation
sum_array = sum(array)
print(sum_array)  # Output: 23
2D Array Operations
1. Rotating a 2D Matrix
One of the common operations on a 2D matrix (list of lists) is rotating it 90 degrees clockwise. The provided implementation rotates the matrix in-place, modifying the original matrix without returning a new one.

Function:

python
Copy code
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
2. Basic Operations
You can perform various operations on 2D arrays, including:

Traversal: Accessing each element or row in the matrix.
Modification: Changing the value of specific elements.
Aggregation: Calculating sums, averages, or other aggregate values for rows, columns, or the entire matrix.
Example:

python
Copy code
# Initialize a 2D array (matrix)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Accessing elements
print(matrix[0][0])  # Output: 1

# Modifying elements
matrix[0][1] = 10
print(matrix)  # Output: [[1, 10, 3], [4, 5, 6], [7, 8, 9]]

# Aggregation
sum_matrix = sum(sum(row) for row in matrix)
print(sum_matrix)  # Output: 45
Usage
To use the rotate_2d_matrix function, simply call it with a 2D matrix as an argument. Ensure the matrix is a square (n x n) for the function to work correctly.

Example:

python
Copy code
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
rotate_2d_matrix(matrix)
print(matrix)

