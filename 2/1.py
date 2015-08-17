"""
Problem 2.1
Write code to remove duplicates from an unsorted linked list.
How would you solve this problem if a temporary buffer is not allowed?
"""


import unittest
from tools import DoublyLinkedList

"""
Naive solution:
Create a deleteNode function that removes nodes from a linked list
and returns the next node in the list. Iterate/recurse through the list,
storing seen node data in a buffer and deleting duplicates.

Runtime: O(n)
Space: O(n)
"""
def naive_solution(list):
    buffer = {}
    temp = list.head
    while temp != None:
        if temp.value in buffer:
            list.deleteNode(temp)
        buffer[temp.value] = True
        temp = temp.next


"""
Revised solution:
Have two runners through the list. One to iterate through the nodes and
another to check for subsequent duplicates.

Runtime: O(n^2)
Space: O(n)
"""
def revised_solution(list):
    iterator = list.head
    while iterator != None:
        checker = iterator.next
        while checker != None:
            if checker.value == iterator.value:
                list.deleteNode(checker)
            checker = checker.next
        iterator = iterator.next


class TestSolution(unittest.TestCase):
    def test_naive(self):
        test_list = DoublyLinkedList.generateExample(True)
        solution_list = DoublyLinkedList.generateExample(False)
        naive_solution(test_list)
        self.assertEqual(test_list.stringify(), solution_list.stringify())

    def test_revised(self):
        test_list = DoublyLinkedList.generateExample(True)
        solution_list = DoublyLinkedList.generateExample(False)
        revised_solution(test_list)
        self.assertEqual(test_list.stringify(), solution_list.stringify())


if __name__ == '__main__':
    unittest.main()
