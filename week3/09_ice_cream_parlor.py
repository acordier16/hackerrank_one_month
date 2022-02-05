#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'icecreamParlor' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER m
#  2. INTEGER_ARRAY arr
#


def icecreamParlor2(m, arr):
    # This is a slow, non-elegant O(n^2) solution
    for i in range(len(arr)):
        for j in range(len(arr)):
            # We filter out non-possible prices (price >= money), and we want distinct flavors
            if i == j or arr[i] >= m or arr[j] >= m:
                continue
            if arr[i] + arr[j] == m:
                return [i + 1, j + 1]  # Offset because 1-indexing


def icecreamParlor(m, arr):
    # A simple, underordered collection as a data structure will allow to check if element is in collection in O(1)
    price_set = set(arr)
    # For each price, we check whether m - arr is present in the price set
    # If it is, we retrieve the indice. This will be done only once, because
    # if it is in the set, then it means we found a solution.
    # Total is O(n) * O(1) + O(n)
    for i, price1 in enumerate(arr):  # O(n)
        if (m - price1) in price_set:  # O(1)
            for j, price2 in enumerate(arr):  # This will be done only once
                if i != j:
                    if price1 + price2 == m:
                        return [i + 1, j + 1]  # Offset because 1_indexing


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    t = int(input().strip())

    for t_itr in range(t):
        m = int(input().strip())

        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = icecreamParlor(m, arr)

        fptr.write(" ".join(map(str, result)))
        fptr.write("\n")

    fptr.close()
