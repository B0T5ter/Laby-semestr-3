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
        else:
            self.tail.next = nowy
        self.tail = nowy
        self.size += 1
    
    def sub(self):
        self.size -= 1
        self.head = self.head.next

    def top(self):
        return self.head.dane
    
def string_to_tokens(expression):
    tokens = []
    num = ""
    
    for char in expression:
        if char.isdigit():
            num += char
        else:
            if num:
                tokens.append(num)
                num = ""
            if char in "+-*/()":
                tokens.append(char)
    
    if num:
        tokens.append(num)
    
    return tokens

# Test
input_data = "(1+2) * 4 + 5 - 3"
output = string_to_tokens(input_data)
print(output)

def zamiana(arr):
    k = Queue()
    s = Stos()
    for x in arr:
        if x.isdigit() == True:
            k.add(x)
        else:
            s.push(x)

        

print(zamiana(output))