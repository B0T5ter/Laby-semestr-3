arr = [4, 2, 2, 1]
key = 3
def hornerItera(arr, key):
    suma = 0 
    n = len(arr)
    for x in range(n):
        #print(arr[x] * key ** (n - x - 1))
        suma += arr[x] * key ** (n - x - 1)
    
    return suma
print(hornerItera(arr, key))

def hornerRek(arr, key):
    if len(arr) == 1:
        return arr[0]
    else:
        return arr[0] * key ** (len(arr) - 1) + hornerRek(arr[1:], key)
    
print(hornerRek(arr, key))