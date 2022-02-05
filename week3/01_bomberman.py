#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'bomberMan' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. STRING_ARRAY grid
#
def explode_grid(grid):
    # input: bomb grid
    # returns: exploded grid
    result_grid = []
    for i in range(len(grid)):
        result_grid.append("")
        for j in range(len(grid[0])):
            a, b, c, d = (False, False, False, False)
            if i > 0:
                a = grid[i - 1][j] == "O"
            if j > 0:
                b = grid[i][j - 1] == "O"
            if i < len(grid) - 1:
                c = grid[i + 1][j] == "O"
            if j < len(grid[0]) - 1:
                d = grid[i][j + 1] == "O"
            e = grid[i][j] == "O"
            if a or b or c or d or e:
                result_grid[-1] += "."
            else:
                result_grid[-1] += "O"
    return result_grid


def bomberMan(n, grid):
    # There is a cycle of repetitive states:
    # t = 0 and t = 1: initial state
    # ---- CYCLE BEGINS ----
    # t = 2: matrix is full of bombs
    # t = 3: explosions of the initial bombs put at t=0
    # t = 4: matrix is full again
    # t = 5: explosions of the bombs put at t=2
    # t = 6: matrix is full again
    # t = 7: explosions of the bombs put at t=4 (this state is the same as t=3)
    # etc.
    if n == 0 or n == 1:
        return grid
    if n % 2 == 0:  # even n
        return ["".join(["O" for i in range(len(grid[0]))]) for i in range(len(grid))]
    else:  # uneven
        if n % 4 == 3:
            return explode_grid(grid)
        if n % 4 == 1:
            return explode_grid(explode_grid(grid))


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    first_multiple_input = input().rstrip().split()

    r = int(first_multiple_input[0])

    c = int(first_multiple_input[1])

    n = int(first_multiple_input[2])

    grid = []

    for _ in range(r):
        grid_item = input()
        grid.append(grid_item)

    result = bomberMan(n, grid)

    fptr.write("\n".join(result))
    fptr.write("\n")

    fptr.close()
