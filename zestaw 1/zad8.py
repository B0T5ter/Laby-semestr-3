import random; arr = [random.randint(-100, 100) for _ in range(10)]
def a(arr):
    ret = 0
    for x in range(len(arr)):
        ret += arr[x]
    return ret

def b(arr):
    ret = 1
    for x in range(len(arr)):
        ret *= arr[x]
    return ret

def c(arr):
    ret = 0
    for x in range(len(arr)):
        ret += arr[x]
    return ret/len(arr)

def d(arr):
    ret = 0
    l = 0
    for x in range(len(arr)):
        if arr[x] > 0:
            ret += arr[x]
            l += 1
    return ret/l

def e(arr):
    ret = 0
    for x in range(len(arr)):
        zwrot = 1
        for y in range(1, x):
            zwrot *= arr[y]
        ret += zwrot
    return ret

print(a(arr))
print(b(arr))
print(c(arr))
print(d(arr))
print(e(arr))