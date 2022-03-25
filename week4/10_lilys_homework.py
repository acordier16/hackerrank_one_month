#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'lilysHomework' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def algo(arr, sorted_arr):
    value_to_indice = {value:i for i, value in enumerate(arr)}
    swaps = 0
    for i in range(len(arr)):
        if arr[i] != sorted_arr[i]:
            # We find the indice which which to swap the current item arr[i]
            indice_to_swap = value_to_indice[sorted_arr[i]]
            # We swap
            current_value = arr[i]
            arr[i], arr[indice_to_swap] = sorted_arr[i], current_value
            # We update index mapping
            value_to_indice[sorted_arr[i]] = i # Note that this line is not needed in practice
            value_to_indice[current_value] = indice_to_swap
            # We increment swaps
            swaps += 1
    return swaps

def lilysHomework(arr):
    """
    We execute the algorithm for the sorted and reverse sorted arrays.
        arr[::] avoids sending the same object to the two
        functions (it creates a copy instead).
    This runs in O(sort + 2*n) = O(sort) = O(n*log(n)) (usually).
    """
    sorted_arr = sorted(arr)
    return min(algo(arr[::], sorted_arr), algo(arr[::], sorted_arr[::-1]))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = lilysHomework(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

