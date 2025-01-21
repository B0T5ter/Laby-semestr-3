def binary(arr, key):
    l = 0
    p = len(arr)
    while l < p:
        s = (l + p)//2
        if key == arr[s]:
            return s
        elif key > arr[s]:
            l = s + 1
        else:
            p = s
    return None

arr = [1,2,3,4,5,6,7,8,9]
print(binary(arr,4))
        