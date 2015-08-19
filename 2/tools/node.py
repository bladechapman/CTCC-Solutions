"""
Defines a linked list node with next, prev, and value attributes
"""
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
    def setValue(self, value):
        self.value = value
    def getValue(self):
        return self.value
    def stringify(self):
        if self.value:
            return '[' + str(self.value) + ']'
        else:
            return '[N]'