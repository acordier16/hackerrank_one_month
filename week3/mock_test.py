"""
Exercise 1: "Truck Tour"
Suppose there is a circle. There are petrol pumps on that circle. Petrol pumps
are numbered 0 to N -1  (both inclusive). You have two pieces of information
corresponding to each of the petrol pump: (1) the amount of petrol that
particular petrol pump will give, and (2) the distance from that petrol pump to
the next petrol pump. Initially, you have a tank of infinite capacity carrying
no petrol. You can start the tour at any of the petrol pumps.
Calculate the first point from where the truck will be able to complete the circle.
Consider that the truck will stop at each of the petrol pumps. The truck will
move one kilometer for each litre of the petrol.
"""


def truckTour(petrolpumps):
    """
    Second solution I wrote in O(n). We can do this because if the
    current computer reservoir becomes negative, then all indexes from the
    last chosen index to the current one are failure points and will not work
    as starting points either. Hence, you don't need to "do it all again".
    """
    n = len(petrolpumps)
    reservoir = 0
    first_index_to_work = 0
    for i, (pump_stock, next_distance) in enumerate(petrolpumps):
        diff = pump_stock - next_distance
        reservoir += diff
        if reservoir < 0:
            reservoir = 0
            first_index_to_work = i + 1
    return first_index_to_work


def truckTourOld(petrolpumps):
    """
    First naive solution I wrote. Not in O(n).
    We build a tree of possibilities, and prune impossible ones as we go.
    """
    n = len(petrolpumps)
    # Initialization: we only select candidates which can go from their point with a zero
    # reservoir to the next pump. Those selected will have their reservoir filled with the initial pump stock.
    # (Note: candidates is an pump_index: current_reservoir dictionary)
    candidates = {
        i: pump_stock
        for i, (pump_stock, next_distance) in enumerate(petrolpumps)
        if pump_stock >= next_distance
    }

    for k in range(1, n + 1):
        new_candidates = {}
        # We compute candidates. Doesn't make sense to try the possibility further
        # if the current station stock + reservoir is smaller than distance to the next
        for index, reservoir in candidates.items():
            _, next_distance = petrolpumps[(index + k - 1) % n]
            next_pump_stock, _ = petrolpumps[(index + k) % n]
            if (
                reservoir >= next_distance
            ):  # If current reservoir is enough to go to next
                reservoir = (
                    reservoir - next_distance + next_pump_stock
                )  # We go to the next station (burns fuel) and refill
                new_candidates[index] = reservoir  # We maintain the possibility
        candidates = new_candidates
    return min(candidates.keys())


"""
Exercise 2: "Pairs"
Given a list of integers and a target value, determine the number of pairs
of the list that have a difference equal to the target value k.
"""


def pairs(k, arr):
    # This problem is very similar to the problem in which you must
    # find the number of pairs (a, b) in a list for which a + b = k
    # Technique is similar, and uses a set (hash table) to get a O(1) retrieval
    # Overall complexity is O(n)

    # Note that the statement does not precise whether a pair can be constitued of the same item,
    # i.e. (a, a), for which the difference would be null. Since k is > 0, this does not matter.
    # Because of this, we do not need to check whether the matched element is the same item or not.
    # Because we also do not need to retrieve the indices of the pairs, this is not O(n * counts).

    arr_set = set(arr)
    counts = 0
    for i, element in enumerate(arr):  # O(n)
        if k + element in arr_set:  # O(1)
            counts += 1
    return counts


"""
Exercise 3: "Big sorting"
Consider an array of numeric strings where each string is a positive number with
anywhere from 1 to 1e6 digits. Sort the array's elements in non-decreasing, or
ascending order of their integer values and return the sorted array.
"""


def bigSorting(unsorted):
    """
    First, we sort the integers by length into different lists.
    Then we sort each list according to natural a-z/1-9 order.
    This allows to sort without casting strings to integers.
    Alternatively, in Python sorted(unsorted, key=int) may work,
    but I don't believe that this is what is asked here.
    """
    max_digits_number = 1000000
    len_to_string = {
        i: [] for i in range(1, max_digits_number)
    }  # Integers should not go beyond 1e6 digits
    for integer in unsorted:
        len_to_string[len(integer)].append(integer)

    sorted_integers = []
    for l in range(1, max_digits_number):
        sorted_integers += sorted(len_to_string[l])

    return sorted_integers
