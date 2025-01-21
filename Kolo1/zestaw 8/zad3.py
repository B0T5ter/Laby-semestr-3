arr = [7,0,3,6,4,3,6,8,9,2,13, -100]
def rekMinMax(arr):
    if arr[0] > arr[1]:
        b = arr[0]
        arr[0] = arr[1]
        arr[1] = b
    n = len(arr)
    if n == 2:
        return arr
    if arr[n-1] < arr[0]:
        arr[0] = arr[n-1]
    if arr[n-1] > arr[1]:
        arr[1] = arr[n-1]
    return rekMinMax(arr[:n - 1])

print(rekMinMax(arr))
   