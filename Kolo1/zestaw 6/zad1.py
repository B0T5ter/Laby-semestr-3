class CycleQueue:
    def __init__(self, n):
        self.arr = [None] * n
        self.head = 0
        self.tail = 0
        self.size = 5
    
    def add(self, dane):
        self.arr[self.tail] = dane
        if self.tail == self.size - 1:
            self.tail = 0
        else:
            self.tail += 1

    def sub(self):
        if self.head == self.size - 1:
            self.head = 0
        else:
            self.head += 1
    
    def top(self):
        return self.arr[self.head]

    def ret_all(self):
        print(self.arr)

a = CycleQueue(5)
a.ret_all()
a.add(1)
a.ret_all()
a.add(2)
a.add(3)
a.add(4)
a.add(5)
a.ret_all()
a.add(6)
a.add(7)
a.ret_all()
print(a.top())
a.sub()
print(a.top())
a.ret_all()