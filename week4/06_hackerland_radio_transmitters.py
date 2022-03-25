#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'hackerlandRadioTransmitters' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY x
#  2. INTEGER k
#

def hackerlandRadioTransmitters2(x, k):
    # First we sort all house coordinates
    x.sort()
    antennas = 0
    # We define a max reaching coordinate
    max_reach = 0
    # We define a target coordinate
    target = 0
    for i in range(len(x)):
        if max_reach < x[i]:
            # We could not reach current x[i]...
            # Set it as next target, and add an antenna in advance
            target = x[i]
            antennas += 1
            max_reach = target + k
        elif x[i] - k <= target:
            max_reach = x[i] + k
    return antennas

def hackerlandRadioTransmitters(x, k):
    """
    This one is easier to understand
    """
    # First we sort all house coordinates
    x.sort()
    antennas = 0
    n = len(x)
    i = 0
    while i < n:
        antennas += 1 # We add the antenna "in advance"

        # Move furthest to the right until we are out of reach
        reach = x[i] + k
        while i < n and x[i] <= reach:
            i += 1

        # Go back from one indice (this is the indice at which we put the antenna)
        i -= 1

        # Checkout the right of the transmitter until we are out of reach
        reach = x[i] + k
        while i < n and x[i] <= reach:
            i += 1
    return antennas

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    x = list(map(int, input().rstrip().split()))

    result = hackerlandRadioTransmitters(x, k)

    fptr.write(str(result) + '\n')

    fptr.close()

