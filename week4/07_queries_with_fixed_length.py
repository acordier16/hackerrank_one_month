#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY arr
#  2. INTEGER_ARRAY queries
#

# Also called sliding max problem (on leetcode)
# Three possibilities:
# - Brute force O(n*k)
# - Priority Queue (or heap) O(n*log(n))
# - Dequeue O(n) (what we do here)

# See for a clear explanation:
# - https://leetcode.com/problems/sliding-window-maximum/discuss/65957/python-solution-with-detailed-explanation

from collections import deque

def add_to_deque(arr, i, dq):
    """
    Adds element indice i to dq.
    This unqueues all indices with corresponding to values higher than arr[i],
    and then appends i.

    The queue looks like: [i_max, ...., i_min]
    Example: [indice_12, indice_9, indice_2], if we want to add indice_13 then
    we unqueue indice_2, indice_9, and indice_12 and then we append indice_13.
    If we want to append indice_3 then we unqueue indice_2 and we append indice_3.

    Note that we store indexes rather than values
    so that we can remove a given index later.
    """
    while dq and arr[dq[-1]] < arr[i]:
        dq.pop()
    dq.append(i)
    return

def solve(arr, queries):
    n = len(arr)
    results = []
    for d in queries:
        dq = deque()
        maxes = []
        # Initialize the queue
        for i in range(d):
            add_to_deque(arr, i, dq)
        maxes.append(arr[dq[0]])
        # Slide the "window queue" starting from indice 1
        for i in range(1, n-d+1):
            # Add new element on the right i+d-1
            add_to_deque(arr, i+d-1, dq)
            # Remove max elements with indice < i ("out of window on the left")
            while dq and dq[0] < i:
                dq.popleft()
            # Append max
            maxes.append(arr[dq[0]])
        results.append(min(maxes))
    return results


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    queries = []

    for _ in range(q):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = solve(arr, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

