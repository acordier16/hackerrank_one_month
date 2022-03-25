#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'roadsAndLibraries' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER c_lib
#  3. INTEGER c_road
#  4. 2D_INTEGER_ARRAY cities
#

class Node:
    def __init__(self, number, neighbors=None):
        self.number = number
        self.neighbors = []
        self.visited = False
    def add_neighbor(self, node):
        self.neighbors.append(node)

from collections import deque
def roadsAndLibraries(n, c_lib, c_road, cities):
    """
    We can think of two extreme cases which are actually the only cases.
    If it's cheaper to build a library than a road, you can simply
        build a library in each city, and min_cost = n * c_lib
    If it's cheaper to build a road than a library, then you need to
        find all blobs and build 1 library per blob, as well as roads
        to connect the cities of the blob (e.g. count the number of cities
        in the blob).
    NB: what I call blob is actually a connected component...
    """
    # The easy case
    if c_lib <= c_road:
        return n*c_lib

    # We build the graph
    nodes = [Node(i) for i in range(1, n+1)]
    for a, b in cities:
        nodes[a-1].add_neighbor(nodes[b-1])
        nodes[b-1].add_neighbor(nodes[a-1])

    components = []
    for i in range(n):
        # If this node was already visited while visiting a previous component, we skip it.
        if nodes[i].visited:
            continue
        # Else we start a new queue for a new component, starting at nodes[i]
        queue = deque([nodes[i]])
        nb_cities = 0 # Number of cities in the component
        nb_roads = 0 # Number of roads to build in the component
        while queue:
            node = queue.pop()
            # We visit the node
            if not node.visited:
                node.visited = True
                nb_cities += 1
                # We loop over its neighbors
                for neighbor in node.neighbors:
                    # If the neighbor hasn't been visited
                    # AND isn't planned to be (this avoids issues with cycles,
                    # i.e. building 1 road too many), we add it to the queue
                    if not neighbor.visited and neighbor not in queue:
                        nb_roads += 1
                        queue.append(neighbor)
        # At this point we visited all nodes of this component
        # We save the number of roads to build and the number of cities
        # for this component
        components.append((nb_roads, nb_cities))

    # Finally, let's compute the minimum price
    minimum_price = 0
    for nb_roads, nb_cities in components:
        # We build nb_roads, and 1 library for the component
        minimum_price += c_road*nb_roads + c_lib*1
    return minimum_price

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        c_lib = int(first_multiple_input[2])

        c_road = int(first_multiple_input[3])

        cities = []

        for _ in range(m):
            cities.append(list(map(int, input().rstrip().split())))

        result = roadsAndLibraries(n, c_lib, c_road, cities)

        fptr.write(str(result) + '\n')

    fptr.close()

