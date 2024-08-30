0x09-island_perimeter
Island Perimeter
This project contains a Python function island_perimeter(grid) that calculates the perimeter of an island represented by a grid of integers.

Table of Contents
Overview
Function Signature
How It Works
Example
Usage
Requirements
Testing
License
Overview
The island_perimeter function determines the perimeter of an island in a grid where:

0 represents water.
1 represents land.
The grid is rectangular, and each cell in the grid is a square with a side length of 1. The function assumes that there is only one island in the grid (or no island) and that the island does not contain any lakes (water that is surrounded by land).

Function Signature
python
Copy code
def island_perimeter(grid):
    """
    Calculate the perimeter of an island in the grid.
    
    Args:
        grid (list of list of int): A 2D list representing the grid where 0 is water and 1 is land.
    
    Returns:
        int: The perimeter of the island.
    """
How It Works
The function iterates over each cell in the grid.
For each land cell (1):
It adds 4 to the perimeter (since each land cell has 4 sides).
It checks the neighboring cells to the left and above. If a neighboring cell is also land, it subtracts 2 from the perimeter for each shared side (since the shared border should not count twice).
This method ensures that the perimeter of the island is calculated correctly.

Example
python
Copy code
if __name__ == "__main__":
    grid = [
        [0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0]
    ]
    print(island_perimeter(grid))  # Output: 12
Explanation:
For the given grid:

csharp
Copy code
[
    [0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0]
]
The function iterates over each cell.
It calculates the perimeter for the island cells in the grid.
The final perimeter of the island is 12.
Usage
Clone the repository or download the script.
Import the island_perimeter function into your Python script.
Pass a 2D list (grid) representing your map as an argument to the function.
python
Copy code
from island_perimeter import island_perimeter

# Example grid
grid = [
    [0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0]
]
print(island_perimeter(grid))  # Expected output: 12
Requirements
Python 3.x
Testing
You can test the function by running the provided example in the 0-main.py script, or you can create your own grid and pass it to the function.

License
This project is licensed under the MIT License - see the LICENSE file for details.

This README should give users a clear understanding of how to use the island_perimeter function, along with an example and explanation of how the function works.








