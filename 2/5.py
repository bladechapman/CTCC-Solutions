"""
Problem 2.5
----------------
You have two numbers represented by a linked list, where each node contains a
single digit. The digits are stored in reverse order, such that the 1's digit
is at the head of the list. Write a function that adds the two numbers and
returns the sum as a linked list
"""


import unittest
from tools import SinglyLinkedList, Node


"""
Naive solution
Iterate through both number lists in parallel. Summed digits must be between 0
and 9, so keep track of the remainder to add to the next node.

Runtime: O(n)
Space: O(n)
"""
def naive_solution(list_1, list_2):
    ret = SinglyLinkedList()
    list_1_iter = list_1.head
    list_2_iter = list_2.head
    remainder = 0
    while (list_1_iter != None or list_2_iter != None):
        a = list_1_iter.getValue() if list_1_iter else 0
        b = list_2_iter.getValue() if list_2_iter else 0

        intermediate_sum = a + b + remainder
        remainder = (int(intermediate_sum / 10)) if (intermediate_sum > 9) else 0

        digit_node = Node(value=(intermediate_sum % 10))
        ret.addNode(digit_node)

        if list_1_iter:
            list_1_iter = list_1_iter.getNext()
        if list_2_iter:
            list_2_iter = list_2_iter.getNext()
    if remainder:
        digit_node = Node(value=remainder)
        ret.addNode(digit_node)

    return ret


class TestSolutions(unittest.TestCase):
    def test_naive(self):
        a = SinglyLinkedList()  # 617
        a.addNode(Node(value=7))
        a.addNode(Node(value=1))
        a.addNode(Node(value=6))

        b = SinglyLinkedList()  # 1055
        b.addNode(Node(value=5))
        b.addNode(Node(value=5))
        b.addNode(Node(value=0))
        b.addNode(Node(value=1))

        sum = naive_solution(a, b)  # 1672
        self.assertEqual(sum.head.getValue(), 2)
        self.assertEqual(sum.head.getNext().getValue(), 7)
        self.assertEqual(sum.head.getNext().getNext().getValue(), 6)
        self.assertEqual(sum.head.getNext().getNext().getNext().getValue(), 1)

if __name__ == '__main__':
    unittest.main()