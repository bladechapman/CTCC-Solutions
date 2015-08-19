"""
Problem 2.3
----------------
Implement an algorithm to to delete a node in the middle of a singly linked
list, given only access to that node
"""


import unittest
from tools import SinglyLinkedList, Node


"""
Naive solution:
Copy the data from the next node into the current node, delete the next node

Runtime: O(1)
Space: O(1)
Caveats:
- If there is only one node in the list, the returned list should be empty
- If the given node is at the end of the list (i.e. the second node in a list
    of two), set the node to None
"""
def naive_solution(node):
    next = node.getNext()
    if next == None:
        node = None
    else:
        node.setValue(next.getValue())
        node.setNext(next.getNext())


class TestSolutions(unittest.TestCase):
    def test_naive(self):
        list = SinglyLinkedList.generateExample()
        mid = list.head
        for i in range(0, 4):
            mid = mid.next
        naive_solution(mid)
        self.assertEqual(list.stringify(), '0 -> 1 -> 2 -> 3 -> 5 -> 6 -> 7 -> 8 -> 9')


if __name__ == '__main__':
    unittest.main()