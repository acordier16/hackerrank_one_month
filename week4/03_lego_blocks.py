#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'legoBlocks' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#

def legoBlocks(n, m):
    """
    We start with height n=1. For this height,
    this is equivalent to a staircase problem with possibility to jump 1, 2, 3, or 4 steps.
    Hence: f(n) = f(n-1) + f(n-2) + f(n-3) + f(n-4)
        (with init f(1) = 1, f(2) = 2, f(3) = 4, f(4) = 8)
    It is equivalent to the staircase problem because the order of blocks DOES matter
        (i.e. we count permutations).
    """
    mod = 10 ** 9 + 7
    m = m % mod
    n = n % mod

    # Compute possibilities for a wall of height n=1, width=m
    cache = [0, 1, 2, 4, 8]
    if m < 5:
        cache = cache[:m+1]
    for i in range(5, m+1):
        cache.append((cache[i-1]+cache[i-2]+cache[i-3]+cache[i-4]) % mod)

    # Now compute all possibilities for a wall of height n, m, for all possible m
    total_possibilities = []
    for i in range(len(cache)):
        total_possibilities.append((cache[i] ** n) % mod)

    # Now we need to get rid of the possibilities with breaks...
    # nb_without_breaks = nb_total - nb_with_breaks
    # and nb_with_breaks(m) = sum(1, m, nb_with_breaks(i)*nb_total(m-i))
    cache2 = [0, 1] + [0]*(m-1)
    for i in range(2, m + 1):
        cache2[i] = total_possibilities[i]
        for j in range(1, i):
            cache2[i] = (cache2[i] - cache2[j] * total_possibilities[i-j]) % mod
    return cache2[-1] % mod

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        result = legoBlocks(n, m)

        fptr.write(str(result) + '\n')

    fptr.close()

