#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'cookies' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY A
#

from heapq import heapify, heappop, heappush


def cookies(k, A):
    """
    To avoid sorting or inserting in a sorted list (with bisect.insort()),
    we use heaps. Heaps are binary trees for which every parent node
    has a value less than or equal to any of its children.
    For the theory on heap (or priority) queue algorithm, check out
    https://docs.python.org/3/library/heapq.html#theory
    Push of the new element is in O(log(n)) (percolate or bubble-up,
    i.e. insert bottom-right and then bubble-up by swapping).
    Pop is in O(log(n)) (bubbling down, i.e. swap the top root element
    downwards until it disappears)
    https://www.youtube.com/watch?v=TdMAsIIM_n8
    This is better than sorting n times (sort algorithms vary from O(n) in best cases to O(n*log(n)) or even O(n^2) in worst cases)
    """
    counter = 0
    heapify(A)  # A[0] will now always return the smallest item
    # The tree is built in linear time
    while A[0] < k:
        if len(A) == 1:
            return -1
        first_smallest = heappop(A)
        second_smallest = heappop(A)
        # This pushes and maintain the order of the tree invariant
        heappush(A, first_smallest + 2 * second_smallest)
        counter += 1
    return counter


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    A = list(map(int, input().rstrip().split()))

    result = cookies(k, A)

    fptr.write(str(result) + "\n")

    fptr.close()
