"""
Problem 2.7
----------------
Given two singly linked lists, determine if the two lists intersect.
Return the intersecting node. Note that the intersection is defined based
on reference, not value. That is, if the kth node of the first linked list
is the exact same node (by reference) as the jth node of the second linked
list, then they are intersecting.
"""


import unittest
from tools import SinglyLinkedList, Node


"""
Naive solution:
Brute force it. Iterate through list 1 and for each node in list 1,
iterate through list 2 to determine if any of the references match. If
they do, return the identical reference.

Runtime: O(n^2)
Space: O(1)
"""
def naive_solution(list_1, list_2):
    list_1_iter = list_1.head
    while (list_1_iter != None):
        list_2_iter = list_2.head
        while (list_2_iter != None):
            if list_1_iter == list_2_iter:
                return list_1_iter
            list_2_iter = list_2_iter.getNext()
        list_1_iter = list_1_iter.getNext()
    return None


"""
Revised solution:
The brute force technique has a lot of repeated work, namely, the second list is
being iterated through n times. One option would be to unfold the loops and store
references of nodes in list 1 as keys to a dictionary. Then, iterate through list 2,
determining if any of the references match.

Runtime: O(n)
Space: O(n)
"""
def revised_solution(list_1, list_2):
    list_1_cache = {}
    list_1_iter = list_1.head
    while list_1_iter != None:
        list_1_cache[list_1_iter] = True
        list_1_iter = list_1_iter.getNext()
    list_2_iter = list_2.head
    while list_2_iter != None:
        if list_2_iter in list_1_cache:
            return list_2_iter
        list_2_iter = list_2_iter.getNext()
    return None


"""
Revised solution 2:
One property of singly linked lists that has not been exploited yet is that
intersecting SLLs can only ever converge, never diverge. Therefore, if there
is ever an intersection, the two lists will always merge into 1, and every node
following the convergence will belong to the same node. This allows us to determine
if an intersection exists in linear time, constant space.

If an intersection is determined to exist, runners can be used to find the difference
in length between the two lists. Using that offset, the two lists can be iterated
in parallel until the first common reference arises.

Runtime: O(n)
Space: O(1)
Caveats: This operation has a higher constant prefex to n, possibly making it slower
on lists of extremely large lengths
"""
def revised_solution_2(list_1, list_2):
    """
    Determine the lengths of each list, determine if the two lists end at the
    same reference
    """
    list_1_iter = list_1.head
    list_2_iter = list_2.head
    if list_1_iter:
        length_1 = 1
    else:
        length_1 = 0
    if list_2_iter:
        length_2 = 1
    else:
        length_2 = 0
    while(list_1_iter.next != None):
        list_1_iter = list_1_iter.next
        length_1 += 1
    while(list_2_iter.next != None):
        list_2_iter = list_2_iter.next
        length_2 += 1
    if list_1_iter != list_2_iter:
        return None
    else:
        """
        Offset the iterator of the longer list so both lists' lengths are
        effectively the same
        """
        list_1_iter = list_1.head
        list_2_iter = list_2.head
        if length_2 > length_1:
            difference = length_2 - length_1
            for i in range(0, difference):
                list_2_iter = list_2_iter.next
        else:
            difference = length_1 - length_2
            for i in range(0, difference):
                list_1_iter = list_1_iter.next
        while list_1_iter != None:
            if list_1_iter == list_2_iter:
                return list_1_iter
            list_1_iter = list_1_iter.next
            list_2_iter = list_2_iter.next
        return None

class TestSolutions(unittest.TestCase):
    def test_naive(self):
        list_1 = SinglyLinkedList.generateExample()
        list_2 = SinglyLinkedList.generateExample()

        intersecting = Node(value=11)
        list_1.addNode(intersecting)
        list_2.addNode(intersecting)

        list_1.addNode(Node(value=99))
        list_1.addNode(Node(value=98))
        list_1.addNode(Node(value=97))

        intersecting_test = naive_solution(list_1, list_2)
        self.assertEqual(intersecting_test, intersecting)
    def test_revised(self):
        list_1 = SinglyLinkedList.generateExample()
        list_2 = SinglyLinkedList.generateExample()

        intersecting = Node(value=11)
        list_1.addNode(intersecting)
        list_2.addNode(intersecting)

        list_1.addNode(Node(value=99))
        list_1.addNode(Node(value=98))
        list_1.addNode(Node(value=97))

        intersecting_test = revised_solution(list_1, list_2)
        self.assertEqual(intersecting_test, intersecting)
    def test_revised_2(self):
        list_1 = SinglyLinkedList.generateExample()
        list_2 = SinglyLinkedList.generateExample()

        intersecting = Node(value=11)
        list_1.addNode(intersecting)
        list_2.addNode(intersecting)

        list_1.addNode(Node(value=99))
        list_1.addNode(Node(value=98))
        list_1.addNode(Node(value=97))

        intersecting_test = revised_solution_2(list_1, list_2)
        self.assertEqual(intersecting_test, intersecting)

if __name__ == '__main__':
    unittest.main()
