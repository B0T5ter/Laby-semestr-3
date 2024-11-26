import random; a = sorted([random.randint(0, 100) for _ in range(10)])
import random; b = sorted([random.randint(0, 100) for _ in range(10)])
#a = [1,2,3]
#b = [1,2,3]
def find(a, b, key):
    x = 0
    y = 0
    while a[x] <= key and x < len(a):
        y = 0
        while y != len(b) and a[x] + b[y] <= key:
            if a[x] + b[y] == key:
                return a[x], b[y]
            y += 1
        x += 1
    return None
print(find(a,b, 50))