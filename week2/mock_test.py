"""
Exercise 1: "Palindrome Index"
Find in a string the index of the character to remove so that the word becomes a palindrome.
"""

def is_palindrome(s):
    return s == list(reversed(s))


def palindromeIndex(s):
    s = list(s)
    n = len(s)
    if is_palindrome(s):
        return -1
    for i in range(n // 2 + 1):
        if s[i] != s[n - i - 1]:  # mismatch
            break
    del s[i]
    if is_palindrome(s):
        return i
    else:
        return len(s) - i

"""
Exercise 2: "Between Two Sets"
There will be two arrays of integers. Determine all integers that satisfy the following two conditions:

The elements of the first array are all factors of the integer being considered
The integer being considered is a factor of all elements of the second array
These numbers are referred to as being between the two arrays. Determine how many such numbers exist.

Example
 a=[2,4]
 b=[24,36]

There are two numbers between the arrays: 6 and 12.
6%2=0, 6%6=0, 24%6=0 and 36%6=0 for the first value.
12%2=0, 12%6=0 and 24%12=0, 36%12=0 for the second value. Return 2.
"""


def getTotalX(a, b):
    counter = 0
    for x in range(min(a), max(b) + 1):
        if all([x % element == 0 for element in a]) and all(
            [element % x == 0 for element in b]
        ):
            counter += 1
    return counter

"""
Exercise 3: "Anagram"
Two words are anagrams of one another if their letters can be rearranged to form the other word.

Given a string, split it into two contiguous substrings of equal length. Determine the minimum number of characters to change to make the two substrings into anagrams of one another.
"""

from collections import Counter

def anagram(s):
    # Idea:
    # Two strings are anagram of each other if the letter count is the same
    s = list(s)
    middle_right_index = len(s) // 2
    s1 = s[:middle_right_index]
    s2 = s[middle_right_index:]
    if len(s1) != len(s2):
        return -1
    counter1 = Counter(s1)
    counter2 = Counter(s2)
    # We now check the "diff" between counter1 and counter 2
    changes = 0
    for letter in counter1.keys():
        counter2.setdefault(letter, 0)
        changes += max(
            counter1[letter] - counter2[letter], 0
        )  # we don't take negative differences to not count the changes "twice"
    return changes
