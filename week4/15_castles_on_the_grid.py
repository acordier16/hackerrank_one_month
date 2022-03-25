#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumMoves' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING_ARRAY grid
#  2. INTEGER startX
#  3. INTEGER startY
#  4. INTEGER goalX
#  5. INTEGER goalY
#

from collections import deque


def minimumMoves(grid, startX, startY, goalX, goalY):
    """
    Important: one "move" is not one "hop"...
    In this problem, one "move" here gives you the possibility
    to move until you encounter an obstacle.
    """
    h = len(grid[0]) - 1
    w = len(grid) - 1
    queue = deque()
    queue.append((startX, startY))
    # This matrix will help us remember which cells
    # we visited and to count the moves as we explore.
    distances = [[None for j in range(len(grid[0]))] for i in range(len(grid))]
    distances[startX][startY] = 0
    # Our queue is first in, last out (append left, pop right)
    while queue:
        currentX, currentY = queue.pop()
        if (currentX, currentY) == (goalX, goalY):
            return distances[currentX][currentY]
        # "Neighbors" for this cell
        # (actually, cells in the 4 directions UNTIL you
        #  find a X cell or a boundary)
        neighbors = []
        # Explore in the right direction until edge or obstacle (x)
        x = currentX + 1
        while x <= w and grid[x][currentY] != "X":
            neighbors.append((x, currentY))
            x += 1
        # Explore in the left direction (x)
        x = currentX - 1
        while x >= 0 and grid[x][currentY] != "X":
            neighbors.append((x, currentY))
            x -= 1
        # Explore in the right direction (y)
        y = currentY + 1
        while y <= h and grid[currentX][y] != "X":
            neighbors.append((currentX, y))
            y += 1
        # Explore in the left direction (y)
        y = currentY - 1
        while y >= 0 and grid[currentX][y] != "X":
            neighbors.append((currentX, y))
            y -= 1
        # Now we decide which neighbors we append to the queue
        for x, y in neighbors:
            # If unexplored cell
            if distances[x][y] is None:
                # Add 1 move for this cell compared to cell of origin
                distances[x][y] = distances[currentX][currentY] + 1
                queue.appendleft((x, y))


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    n = int(input().strip())

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    first_multiple_input = input().rstrip().split()

    startX = int(first_multiple_input[0])

    startY = int(first_multiple_input[1])

    goalX = int(first_multiple_input[2])

    goalY = int(first_multiple_input[3])

    result = minimumMoves(grid, startX, startY, goalX, goalY)

    fptr.write(str(result) + "\n")

    fptr.close()
