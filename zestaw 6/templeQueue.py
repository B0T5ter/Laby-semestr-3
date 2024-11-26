class Node:
    def __init__(self, dane = None, next = None):
        self.dane = dane
        self.next = next
    
class Queue:
    def __init__(self):
        self.tail = None
        self.head = None
        self.size = 0
    
    def add(self, dane):
        nowy = Node(dane)
        if self.size == 0:
            self.head = nowy
        elif self.size:
            self.tail.next = nowy
        self.tail = nowy
        self.size += 1
    
    def sub(self):
        self.size -= 1
        self.head = self.head.next

    def top(self):
        return self.head.dane
    
a = Queue()
a.add(1)
print(a.top())
a.add(2)
print(a.top())
a.sub()
print(a.top())