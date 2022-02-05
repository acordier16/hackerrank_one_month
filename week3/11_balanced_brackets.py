#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'isBalanced' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#


def isBalanced(s):
    # Better solution with an actual stack.
    # The idea is to cross-checks all brackets.
    # This is in O(n)
    s = list(s)
    d = {"}": "{", "]": "[", ")": "("}
    right_brackets = d.keys()
    left_brackets = d.values()
    stack = []
    for c in s:
        if c in left_brackets:
            stack.append(c)
        elif c in right_brackets:
            # If stack is empty or previous left bracket is not matching with this right bracket,
            # something is wrong...
            if (not stack) or stack.pop() != d[c]:
                return "NO"
    # If stack is empty at the end, string is valid
    if not stack:
        return "YES"
    return "NO"


def isBalancedOld(s):
    # This algorithm is in O(n * nb_nested_levels).
    # Basically we loop through the string until we have
    # eliminated all matches.
    # We could also do it in fewer lines with .replace("()", "")...
    s = list(s)
    d = {"{": "}", "[": "]", "(": ")"}
    left_brackets = d.keys()
    right_brackets = d.values()

    # If the first character is not a left bracket, we can discard it immediately
    if s[0] not in left_brackets:
        return "NO"

    stack = s
    while len(stack) > 2:
        new_stack = []
        flag = False
        for i in range(len(stack) - 1):
            if stack[i] in left_brackets:
                # If we match two consecutive characters (left -> right),
                # we discard them in the stack we are building
                if d[stack[i]] == stack[i + 1]:
                    flag = True  # This flag purpose is to not take the following right character
                    continue
            if flag:
                flag = False
            else:
                new_stack.append(stack[i])
        # Last character is appended in anycase
        new_stack.append(stack[-1])
        # If the stack has not changed, it means we could not cross anything,
        # hence something is wrong and the string is not balanced
        if new_stack == stack:
            return "NO"
        # Update the stack
        stack = new_stack

    # At this point we should have only two elements in our final stack
    if stack[0] not in left_brackets or d[stack[0]] == stack[1]:
        return "YES"
    else:
        return "NO"


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    t = int(input().strip())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + "\n")

    fptr.close()
