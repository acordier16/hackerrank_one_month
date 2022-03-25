#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'highestValuePalindrome' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER n
#  3. INTEGER k
#

def highestValuePalindrome(s, n, k):
    # Edge case
    if n == 1:
        if k >= 1: return "9"
        else: return s

    s = [int(x) for x in list(s)]
    moves_left = k
    moves_memory = [0] * (n // 2) + [1]
    # First we make sure that it possible to build a palindrome
    for i in range(n // 2):
        if s[i] > s[n-i-1]:
            s[n-i-1] = s[i]
            moves_left -= 1
            moves_memory[i] += 1
        elif s[i] < s[n-i-1]:
            s[i] = s[n-i-1]
            moves_left -= 1
            moves_memory[i] += 1
        if moves_left < 0:
            return "-1"
    # At this point we built a palindrome
    # While we have moves left, we change adequate values to "9"
    for i in range((n // 2) + 1):
        if moves_left == 0:
            break
        if s[i] == 9:
            continue
        # We did not touch i and n-i-1 previously, changing both to 9 costs 2
        if moves_memory[i] == 0 and moves_left >= 2:
            s[i] = 9
            s[n-i-1] = 9
            moves_left -= 2
        # We already changed i or n-i-1, so changing both to 9 costs 1
        # (this is also the code to execute for the middle letter in case
        # of uneven n)
        elif moves_memory[i] == 1 and moves_left >= 1:
            s[i] = 9
            s[n-i-1] = 9
            moves_left -= 1
    return "".join([str(x) for x in s])

if __name__ == '__main__':

    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    s = input()

    result = highestValuePalindrome(s, n, k)

    fptr.write(result + '\n')
    fptr.close()

