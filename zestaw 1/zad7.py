import random; arr = [random.randint(0, 100) for _ in range(10)]
def miniMax(arr):
    retmax = arr[0]
    retmin = arr[0]
    for x in range(1, len(arr)):
        if arr[x] > retmax:
            retmax = arr[x]
        if arr[x] < retmin:
            retmin = arr[x]
    return retmin, retmax

print(arr)
print(miniMax(arr))