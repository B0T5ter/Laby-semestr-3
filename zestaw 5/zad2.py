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
    a = Stos()
    for x in arr:
        if x in "{[(":
            a.push(x)
        elif x == '}' and a.top() == "{":
            a.pop()
        elif x == ']' and a.top() == "[":
            a.pop()
        elif x == ')' and a.top() == "(":
            a.pop()
        else:
            return False
    return True

arr = "({[]})"
print(sprawdzenie(arr))

arr = "([})"
print(sprawdzenie(arr))
