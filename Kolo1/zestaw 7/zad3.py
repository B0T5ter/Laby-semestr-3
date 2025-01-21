class Stos:
    def __init__(self):
        self.arr = []
        self.size = 0
        self.max_size = 99

    def push(self, x):
        if self.size < self.max_size:
            self.arr.append(x)
            self.size += 1
            return
        else:
            print("Stos jest pełen")
    
    def pop(self):
        if self.size > 0:
            self.arr.pop(len(self.arr) - 1)
            self.size -= 1
        else:
            print("Stos jest pusty")
    
    def top(self):
        if self.size > 0:
            return self.arr[len(self.arr) - 1]
        else:
            print("Stos jest pusty")

class Queue:
    def __init__(self):
        self.stos1 = Stos()
        self.stos2 = Stos()
        self.size = 0
        self.max_size = 10

    def add(self,x):
        if self.size < self.max_size:
            self.stos1.push(x)
        else:
            print("Kolejka jest pełna")
    
    def sub(self):
        while self.stos1.size != 1:
            self.stos2.push(self.stos1.top())
            self.stos1.pop()
        self.stos1.pop() 
        while self.stos2.size != 0:
            self.stos1.push(self.stos2.top())
            self.stos2.pop()

    def prawa(self):
        while self.stos1.size != 1:
            self.stos2.push(self.stos1.top())
            self.stos1.pop()
        print(self.stos1.top())
        while self.stos2.size != 0:
            self.stos1.push(self.stos2.top())
            self.stos2.pop()
    
    def ret_all(self):
        print(self.stos1.arr[::-1])
a = Queue()
a.add(1)
a.add(2)
a.add(3)
a.add(4)
a.add(5)
a.prawa()
a.sub()
a.ret_all()