#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'waiter' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY number
#  2. INTEGER q
#


def generate_primes(n):
    # Eratosthene algorithm to generate primes
    primes = []
    for i in range(2, n + 1):
        if i in [2, 3, 5]:
            primes.append(i)
            continue
        if all([i % prime != 0 for prime in primes]):
            primes.append(i)
    return primes


primes = generate_primes(10000)  # Generates at least 1200 primes


def waiter(number, q):
    # In essence, this requires to write a primality test (see above).
    # The rest is not too complicated
    # (it's just the problem that is poorly written!)
    a = number
    b = []
    answers = []
    for i in range(q):
        new_a = []
        while a:
            top_element = a.pop()
            if top_element % primes[i] != 0:
                new_a.append(top_element)
            else:
                b.append(top_element)
        a = new_a
        # We pop the B queue into answers
        while b:
            answers.append(b.pop())
    # When iterations are over, we pop the A queue into answers
    while a:
        answers.append(a.pop())
    return answers


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    number = list(map(int, input().rstrip().split()))

    result = waiter(number, q)

    fptr.write("\n".join(map(str, result)))
    fptr.write("\n")

    fptr.close()
