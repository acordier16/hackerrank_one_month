#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'noPrefix' function below.
#
# The function accepts STRING_ARRAY words as parameter.
#

from collections import defaultdict
def Trie(): return defaultdict(Trie)

def add_word_to_trie(trie, word):
    if len(word) == 0: # We are finished with decomposing our word
        if len(trie) > 0: # The path to go to this word is not 0, meaning the current word
                          # is a prefix of a previous word
            return False
        trie[word] = ""
        return True
    if "" in trie: # We already have a a word in the past which is a prefix of the current one
        return False
    return add_word_to_trie(trie[word[0]], word[1:])

def noPrefix(words):
    """
    This solution was proposed by pdog1111 on HR forum.
    I could not have succeeded without his Trie implementation.
    """
    trie = Trie()
    for word in words:
        if not add_word_to_trie(trie, word):
            print("BAD SET")
            print(word)
            return
    print("GOOD SET")
    return

if __name__ == '__main__':
    n = int(input().strip())

    words = []

    for _ in range(n):
        words_item = input()
        words.append(words_item)

    noPrefix(words)
