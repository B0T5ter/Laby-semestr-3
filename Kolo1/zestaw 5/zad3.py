class Stos:
    def __init__(self):
        self.arr = []
    
    def isEmpty(self):
        return len(self.arr) == 0
    
    def push(self, x):
        self.arr.append(x)
    
    def pop(self):
        if self.isEmpty() == False:
            self.arr.pop()
            return
        print("Stos jest pusty")
    
    def top(self):
        if self.isEmpty() == False:
            return self.arr[len(self.arr) - 1]
        print("Stos jest pusty")

    def size(self):
        print(len(self.arr))



def sprawdzenie(arr):
    b = Stos()
    odp = []
    y = 1
    for x in arr:
        if x == "(":
            b.push(y)
            odp.append(y)
            y += 1
        elif x == ')':
            odp.append(b.top())
            b.pop()
        
    return odp

arr = "((()(())))"
print(sprawdzenie(arr))

