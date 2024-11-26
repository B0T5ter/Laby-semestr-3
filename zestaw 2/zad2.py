arr = [1,2,3,3,3,2,3,3,4,5]
def lider(arr):
    ret = arr[0]
    licze = 1
    for x in range(1, len(arr)):
        if arr[x] == ret:
            licze += 1
            continue
        if arr[x] != ret:
            licze -= 1
        if licze == 0:
            ret = arr[x]
            licze += 1

    licze = 0
    for x in arr:
        if x == ret:
            licze += 1
    if licze >= len(arr)//2:
        return ret
    return None

print(lider(arr))