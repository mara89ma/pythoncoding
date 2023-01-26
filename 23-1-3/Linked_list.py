def add(self, value):
    new_node = Node(value)
    if self.head is None:
        self.head = new_node
        self.tail = new_node
        self.current = new_node
    else:
        self.tail.next_node = new_node
        self.tail = new_node
        
class Node:
def init(self, value=None, next_node=None):
self.value = value
self.next_node = next_node

class LinkedList:
def init(self):
self.head = None
self.tail = None
self.current = None
def delete(self):
    if self.head is None:
        return None
    if self.head == self.tail:
        value = self.head.value
        self.head = None
        self.tail = None
        self.current = None
        return value
    if self.current == self.head:
        value = self.head.value
        self.head = self.head.next_node
        self.current = self.head
        return value
    else:
        previous = self.head
        while previous.next_node != self.current:
            previous = previous.next_node
        value = self.current.value
        previous.next_node = self.current.next_node
        if self.current == self.tail:
            self.tail = previous
        self.current = self.current.next_node
        return value
def get(self):
    if self.current:
        return self.current.value
    else:
        return None
def move_next(self):
    if self.current:
        self.current = self.current.next_node
def move_front(self):
    self.current = self.head
