#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'climbingLeaderboard' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player
#


def climbingLeaderboard(ranked, player):
    player_ranks = []
    # I wanted to do this with a Counter at first, but it is
    # even simpler by doing: list -> set -> list -> sort().
    ranked_set = sorted(list(set(ranked)), reverse=True)
    rank = len(ranked_set)
    # Second optimization here (which I had not done at first) is that,
    # since the player ranks are already ordered,
    # we can remember where we stopped in the ranks
    # when checking out the next player score.
    # Thanks to albiewalbie user on the HR forum.
    for player_score in player:
        while rank > 0 and player_score >= ranked_set[rank - 1]:
            rank -= 1
        player_ranks.append(rank + 1)
    return player_ranks


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)

    fptr.write("\n".join(map(str, result)))
    fptr.write("\n")

    fptr.close()
