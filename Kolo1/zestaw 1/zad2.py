import random; arr = [random.randint(0, 100) for _ in range(10)]
def miniFor(arr):
    ret = arr[0]
    for x in range(1, len(arr)):
        if arr[x] < ret:
            ret = arr[x]
    return ret

print(arr)
print(miniFor(arr))