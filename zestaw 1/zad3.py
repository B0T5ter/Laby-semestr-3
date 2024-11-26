import random; arr = [random.randint(0, 100) for _ in range(10)]
def miniInd(arr):
    ret = arr[0]
    ind = 0
    for x in range(1, len(arr)):
        if arr[x] < ret:
            ret = arr[x]
            ind = x
    return ret, ind

print(arr)
print(miniInd(arr))