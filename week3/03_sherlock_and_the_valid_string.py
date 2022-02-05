#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'isValid' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

# Can also be handled with a collections.Counter object in Python
def count(s):
    counter = dict()
    for c in s:
        counter.setdefault(c, 0)
        counter[c] += 1
    return counter


def isValid(s):
    s = list(s)
    frequencies = count(s).values()
    print(count(s))
    frequencies_of_frequencies = count(frequencies)
    keys = frequencies_of_frequencies.keys()
    values = frequencies_of_frequencies.values()

    # String is already valid
    if len(values) == 1:
        return "YES"
    elif len(values) > 2:
        return "NO"
    else:  ## len(values) == 2
        if min(values) == 1:
            k1 = min(keys)
            k2 = max(keys)
            if frequencies_of_frequencies[k1] == 1 or k2 - k1 == 1:
                return "YES"
        return "NO"

    # This can probably be optimized as we can gather the max while we count
    max_frequency = max(frequencies)
    min_frequency = min(frequencies)
    print(frequency)
    # nb_to_remove = sum([(max_frequency - frequency) > 1 \
    #                    for frequency in frequencies])
    if max_frequency - min_frequency >= 1:
        return "NO"
    else:
        return "YES"


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    s = input()

    result = isValid(s)

    fptr.write(result + "\n")

    fptr.close()
