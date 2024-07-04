def pascal_triangle(n):
    """
    Pascal's Triangle up to n rows.

    Parameters:
    - n (int): Number of rows to generate in the Pascal's Triangle.

    Returns:
    - list of lists: Pascal's Triangle represented as a list of lists,
      where each inner list corresponds to a row in the triangle.

    Edge Case:
    - If n is 0, an empty list is returned.

    Algorithm:
    - Initialize the triangle with the first row [1].
    - For each subsequent row from 1 to n-1:
      - Retrieve the previous row.
      - Start a new row with [1].
      - Calculate each element in the new row (excluding the ends)
        as the sum of the two adjacent elements from the previous row.
      - End the new row with [1].
      - Append the new row to the triangle.

    Example:
    >>> generate_pascals_triangle(5)
    [[1],
     [1, 1],
     [1, 2, 1],
     [1, 3, 3, 1],
     [1, 4, 6, 4, 1]]
    """
    if n == 0:
        return []  

    triangle = [[1]]  

    for i in range(1, n):
        prev_row = triangle[-1]  
        new_row = [1]  

        for j in range(1, i):
            new_value = prev_row[j-1] + prev_row[j]  
            new_row.append(new_value)

        new_row.append(1)  
        triangle.append(new_row)  
    
    return triangle

