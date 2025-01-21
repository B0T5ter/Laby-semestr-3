def search(arr, key):
    if arr[0] == key:
        return True
    if len(arr) != 1:
        return search(arr[1:], key)
    return False
arr = [1,2,3]
print(search(arr,5))
