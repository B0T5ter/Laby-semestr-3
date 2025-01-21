import random; arr = [random.randint(0, 100) for _ in range(10)]
def miniWhile(arr):
    x = 1
    ret = arr[0]
    while x < len(arr):
        if arr[x] < ret:
            ret = arr[x]
        x += 1
    return ret

print(arr)
print(miniWhile(arr))