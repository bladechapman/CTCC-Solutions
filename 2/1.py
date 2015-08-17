"""
Problem 2.1
Write code to remove duplicates from an unsorted linked list.
How would you solve this problem if a temporary buffer is not allowed?
"""


import unittest


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


class LinkedList():
    def __init__(self, **kwargs):
        self.head = kwargs['head'] if 'head' in kwargs else None

    def addNode(self, node):
        if self.head == None:
            self.head = node
            return self.head
        else:
            temp = self.head
            while temp.getNext() != None:
                temp = temp.getNext()
            temp.setNext(node)
            node.setPrev(temp)

            return self.head
    def deleteNode(self, node):
        if (node == self.head):
            self.head = node.next

        prev = node.prev
        next = node.next
        if prev: prev.next = next
        if next: next.prev = prev
    def stringify(self):
        temp = self.head
        ret = ''
        while temp != None:
            if temp == self.head:
                ret += str(temp.getValue())
            else:
                ret += ' -> ' + str(temp.getValue())
            temp = temp.getNext()
        return ret

    @staticmethod
    def generateExample(doubleNodes):
        list = LinkedList()
        node_to_remove = None
        for i in range(0, 10):
            node_1 = Node(value=i)
            node_2 = Node(value=i)
            list.addNode(node_1)
            if doubleNodes: list.addNode(node_2)
        return list


class Node():
    def __init__(self, **kwargs):
        self.next = kwargs['next'] if 'next' in kwargs else None
        self.prev = kwargs['prev'] if 'prev' in kwargs else None
        self.value = kwargs['value'] if 'value' in kwargs else 0

    def setNext(self, next):
        self.next = next
    def getNext(self):
        return self.next
    def setPrev(self, prev):
        self.prev = prev
    def getPrev(self):
        return self.prev

    def getValue(self):
        return self.value


class TestSolution(unittest.TestCase):
    def test_naive(self):
        test_list = LinkedList.generateExample(True)
        solution_list = LinkedList.generateExample(False)
        naive_solution(test_list)
        self.assertEqual(test_list.stringify(), solution_list.stringify())

    def test_revised(self):
        test_list = LinkedList.generateExample(True)
        solution_list = LinkedList.generateExample(False)
        revised_solution(test_list)
        self.assertEqual(test_list.stringify(), solution_list.stringify())


if __name__ == '__main__':
    unittest.main()
