#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maxSubarray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def maxSubarray(arr):
    """
    If all negatives, max subarray is of size 1 with the max element.
    If all positives, max subarray is the array itself.
    If mix of positives/negatives, max subarray is the array with only positive numbers.
    """
    cache = [arr[0]] # We use dp for max sub-array
    #cache2 = [arr[0]] # We could use dp also for max sub-sequence
    sum2 = arr[0] # But it's too costly compared to doing it with this variable (saving max as we go)
    for i in range(1, len(arr)):
        cache.append(max(arr[i], cache[i-1] + arr[i])) # contiguous subsequence
        #cache2.append(max(arr[i], max(cache2) + arr[i])) # subsequence (with dp)
        sum2 = max(max(sum2, arr[i]), sum2+arr[i]) # subsequence (with single variable)
    #return [max(cache), max(cache2)]
    return [max(cache), sum2]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = maxSubarray(arr)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()

