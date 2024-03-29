from . import Node

"""
Defines a singly linked list using the Node class
"""
class SinglyLinkedList():
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
    def deleteNode(self, node):
        if self.head == node:
            self.head = node.getNext()
            return self.head
        else:
            temp = self.head
            while temp.getNext() != node:
                temp = temp.getNext()
            prev = temp
            next = node.getNext()
            prev.setNext(next)
    def stringify(self):
        buffer = ''
        temp = self.head
        while temp != None:
            if temp == self.head:
                buffer += str(temp.getValue())
            else:
                buffer += ' -> ' + str(temp.getValue())
            temp = temp.getNext()
        return buffer

    @staticmethod
    def generateExample():
        list = SinglyLinkedList()
        for i in range(0, 10):
            node = Node(value=i)
            list.addNode(node)
        return list


"""
Defines a doubly linked list using the Node class
"""
class DoublyLinkedList():
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
                ret += ' <-> ' + str(temp.getValue())
            temp = temp.getNext()
        return ret

    @staticmethod
    def generateExample(doubleNodes=False):
        list = DoublyLinkedList()
        node_to_remove = None
        for i in range(0, 10):
            node_1 = Node(value=i)
            node_2 = Node(value=i)
            list.addNode(node_1)
            if doubleNodes: list.addNode(node_2)
        return list