"""
Problem 2.2
----------------
Implement an algorithm to find the kth last element in
a singly linked list
"""


import unittest
from tools import SinglyLinkedList


"""
Naive solution:
Recurse through the list. Upon reaching the bottom, return a tuple
with the current depth from the end, and a variable representing the
kth element from the bottom.

Runtime: O(n)
Space: O(n)
"""
def naive_solution(list, k):
    d, n = naive_solution_recursive(list.head, k)
    return n
def naive_solution_recursive(node, k):
    if node == None:
        return (1, None)
    d, n = naive_solution_recursive(node.next, k)
    if n:
        return (d + 1, n)
    elif d == k:
        return (d + 1, node)
    else:
        return (d + 1, None)


"""
Revised solution:
Use two runners, a and b. Move runner a into the linked list by k nodes.
Then, place b at the beginning of the linked list and move both runners
at equal pace until runner a hits the end of the list. At that point, runner
b will be on the kth last element from the end.

Runtime: O(n)
Space: O(1)
"""
def revised_solution(list, k):
    a = list.head
    b = None
    for i in range(0, k - 1):
        if a == None:
            return b
        a = a.getNext()
    while a != None:
        if b == None:
            b = list.head
        else:
            b = b.getNext()
        a = a.getNext()
    return b


class TestSolutions(unittest.TestCase):
    def test_naive(self):
        test_list = SinglyLinkedList.generateExample()
        self.assertEqual(naive_solution(test_list, 2).value, 8)
        self.assertEqual(naive_solution(test_list, 12), None)

    def test_revised(self):
        test_list = SinglyLinkedList.generateExample()
        self.assertEqual(revised_solution(test_list, 2).value, 8)
        self.assertEqual(revised_solution(test_list, 12), None)

if __name__ == '__main__':
    unittest.main()