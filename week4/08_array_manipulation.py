#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'arrayManipulation' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def arrayManipulation2(n, queries):
    """
    Building the array in a dp-fashion.
    This is O(n*nb_queries)
    """
    cache = [0] * n
    for i in range(n):
        for start, end, k in queries:
            # If this indice is not considered by the query, skip the query
            if not (start <= i+1 and i+1 <= end):
                continue
            cache[i] += k
    return max(cache)

def arrayManipulation(n, queries):
    """
    We are only interested by the max!
    We don't need to build the array...
    This is a trick-based problem. You need to find the trick
    or you will not find a O(n+nb_queries) solution.
    Very nice exercise however!
    """

    cache = [0] * (n+1)
    for start, end, k in queries:
        cache[start-1] += k
        cache[end-1 + 1] -= k

    # We estimate the (pseudo-)slope at every value.
    # This is done by cumulating the values of our cache.
    max_slope = 0
    cumulated_sum = 0
    for i in range(n+1):
        cumulated_sum += cache[i]
        max_slope = max(max_slope, cumulated_sum)
    return max_slope

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()

