# Enter your code here. Read input from STDIN. Print output to STDOUT

from heapq import heapify, heappop, heappush
import os

# Note that the heap (priority queue) data structure is not made for
# removing a specific element... but only the min!
# (or max depending on implementation)
# Hence we rely on an additional hashtable (set data structure in python)
# for removing these specific element when printing the minimum.

fptr = open(os.environ['OUTPUT_PATH'], 'w')

nb_queries = int(input().rstrip())

A = []
A_set = set()
heapify(A)

for i in range(nb_queries):
    query = input().rstrip().split()
    query_type = int(query[0])
    if query_type in [1, 2]:
        query_value = int(query[1])
        if query_type == 1:
            heappush(A, query_value)
            A_set.add(query_value)
        elif query_type == 2:
            A_set.discard(query_value)
    else:
        while A[0] not in A_set:
            heappop(A)
        fptr.write(str(A[0]) + '\n')

fptr.close()

