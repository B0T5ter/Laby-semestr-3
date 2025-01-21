import random; arr = [random.randint(0, 100) for _ in range(10)]
def selection_sort(arr):
    for x in range(len(arr)):
        akt = arr[x]
        ind = x
        for y in range(x, len(arr)):
            if arr[y] < akt:
                akt = arr[y]
                ind = y
        if akt != arr[x]:
            arr[ind] = arr[x]
            arr[x] = akt
    return arr

def insertion_sort(arr):
    for x in range(1, len(arr)):
        akt = arr[x]
        y = x
        while y != 0 and akt > arr[y]:
            arr[y] = arr[y - 1]
            y -= 1
        arr[y] = akt
    return arr
a = selection_sort(arr)
b = insertion_sort(arr)


licza = 1
for x in range(1, len(a)):
    if a[x] != a[x - 1]:
        licza += 1

liczb = 1
for x in range(1, len(b)):
    if b[x] != b[x - 1]:
        liczb += 1
print(a)
print(licza)
print(b)
print(liczb)