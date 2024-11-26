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

    def all_out(self):
        print(self.arr)
def obrobka(a):
    aktu = ""
    arr = []
    for x in a:
        if x == " ":
            try:
                arr.append(int(aktu))
            except:
                arr.append(aktu)
            aktu = ""
        else:
            aktu += x
    try:
        arr.append(int(aktu))
    except:
        arr.append(aktu)
    return arr

a = '20 10 + 75 45 - *'
#a = '20 10 + 10 +'
arr = obrobka(a)

def liczenie(arr):
    z = Stos()
    a = None
    b = None
    for x in arr:
        z.all_out()
        if x == "+" or x == "-" or x == '/' or x == "*":
            a = z.top()
            z.pop()
            b = z.top()
            z.pop()
            if x == "+":
                odp = a + b
            if x == "-":
                odp = b - a
            if x == "*":
                odp = (a * b)
            if x == "/":
                odp = (a / b)
            z.push(odp)
        else:
            z.push(x)
    return z.top()

print(liczenie(arr))

