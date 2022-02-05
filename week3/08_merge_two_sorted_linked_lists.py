#!/bin/python3

import math
import os
import random
import re
import sys


class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node

        self.tail = node


def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)


# Complete the mergeLists function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#


def mergeLists(head1, head2):
    # We need to return a merged AND sorted list...
    # Assuming (not precised in the problem!) that the two input lists
    # are already sorted.
    # NB: if the merged list did not need to be sorted, condition would not
    # be a.data < b.data, but rather index % 2 == 0.

    index = 0
    a = head1
    b = head2
    while not (a is None and b is None):
        # If both lists are not ended, and a is lower than b, then insert a.
        # Or, if b is ended, then also insert a.
        if (a is not None and b is not None and a.data < b.data) or b is None:
            data = a.data
            a = a.next
        # Conversely, insert b.
        elif (a is not None and b is not None and b.data >= b.data) or a is None:
            data = b.data
            b = b.next

        # Build the new merged list
        if index == 0:
            new_head = SinglyLinkedListNode(node_data=data)
            previous_node = new_head
        else:
            new_node = SinglyLinkedListNode(node_data=data)
            previous_node.next = new_node
            previous_node = new_node
        index += 1
    return new_head


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    tests = int(input())

    for tests_itr in range(tests):
        llist1_count = int(input())

        llist1 = SinglyLinkedList()

        for _ in range(llist1_count):
            llist1_item = int(input())
            llist1.insert_node(llist1_item)

        llist2_count = int(input())

        llist2 = SinglyLinkedList()

        for _ in range(llist2_count):
            llist2_item = int(input())
            llist2.insert_node(llist2_item)

        llist3 = mergeLists(llist1.head, llist2.head)

        print_singly_linked_list(llist3, " ", fptr)
        fptr.write("\n")

    fptr.close()
