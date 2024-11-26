def search(arr, key):
    if len(arr) == 0:
        return False
    if arr[0] == key:
        return True
    return search(arr[1:], key)

arr = [0,1,2,3,4,5]
print(search(arr,3))