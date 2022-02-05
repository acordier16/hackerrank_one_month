#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.
#

def minimumBribes(q):
    #print(q)
    total_bribes = 0
    for i in range(len(q)):
        bribes = max(q[i] - (i+1), 0)
        if bribes > 2:
            print("Too chaotic")
            return None

        # We need to count the bribes RECEIVED by each individual
        # Example: [1, 2, 5, 3, 7, 8, 6, 4]
        # Person 4 has been bribed 4 times because he has person 5, 6, 7, and 8 in front of him
        # Here, we count the nb of people in front of person i with higher number
        # (No need to count from the beginning of the queue, since if they bribed him, they can
        # only be max 2 persons ahead of him)
        minimum_bribes_received = sum([q[j] > q[i] for j in range(max(q[i]-2, 0), i)])
        total_bribes += minimum_bribes_received
    print(total_bribes)

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
