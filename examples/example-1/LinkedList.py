from List import *

class LinkedList(List):
    class Node:
        def __init__(self, value, next):
            self.value = value
            self.next = next

    def __init__(self, size):
        super().__init__(size)
        self.head = None
        self.tail = None
        self.cnt = 0

    def add(self, value):
        if self.cnt == self.size:
            return  # TODO - raise an error

        if self.tail != None:
            self.tail.next = LinkedList.Node(value, None)
            self.tail = self.tail.next
        else:
            self.head = self.tail = LinkedList.Node(value, None)
        self.cnt += 1

    def remove(self):
        if self.cnt == 0:
            pass  # TODO - raise an error
        else:
            self.cnt -= 1
            value = self.tail.value
            if self.head == self.tail:
                self.head = self.tail = None
            else:
                current = self.head
                while current.next != self.tail:
                    current = current.next
                self.tail = current
                self.tail.next = None
            return value

    def gettext(self):
        current = self.head
        value = ''
        while current != None:
            value += '(' + str(current.value) + ')'
            current = current.next
        return value


