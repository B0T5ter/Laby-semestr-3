class Stos:
    def __init__(self):
        self.arr = []

    def push(self,x):
        self.arr.append(x)
    
    def isEmpty(self):
        return len(self.arr) == 0
    
    def pop(self):
        if self.isEmpty() == False:
            self.arr.pop()
    
    def top(self):
        if self.isEmpty() == False:
            print(self.arr[len(self.arr) - 1])
    
    def size(self):
        print(len(self.arr))

a = Stos()
a.push(1)
a.top()