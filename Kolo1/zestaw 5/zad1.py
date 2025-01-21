class Stos:
    def __init__(self):
        self.arr = []
    
    def isEmpty(self):
        return self.size() == 0
    
    def push(self, x):
        self.arr.insert(0, x)
    
    def pop(self):
        if self.isEmpty() == False:
            self.arr.pop()
            return
        print("Stos jest pusty")
    
    def top(self):
        if self.isEmpty() == False:
            print(self.arr[self.size() - 1])
            return
        print("Stos jest pusty")

    def size(self):
        return len(self.arr)

a = Stos()
a.push(1)
a.push(2)
a.top()
