import random
import time
import matplotlib.pyplot as plt

def generator(n,min = -100, max = 100):
    arr = []
    for x in range(n):
        los = random.randint(min, max)
        arr.append(los)
    return arr


def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    
    srodek = len(arr)//2
    lewa = mergeSort(arr[:srodek])
    prawa = mergeSort(arr[srodek:])

    return merge(lewa, prawa)

def merge(lewa, prawa):

    ret = []
    i = j = 0

    while i < len(lewa) and j < len(prawa):
        if lewa[i] < prawa[j]:
            ret.append(lewa[i])
            i += 1
        else:
            ret.append(prawa[j])
            j += 1

    while i < len(lewa):
        ret.append(lewa[i])
        i += 1
    while j < len(prawa):
        ret.append(prawa[j])
        j += 1
    return ret


def quickSort(arr):
    n = len(arr)
    if n <= 1:
        return arr
    srodek = arr[n - 1]
    lewa = []
    prawa = []
    for x in range(n - 1):
        if arr[x] < srodek:
            lewa.append(arr[x])
        else:
            prawa.append(arr[x])
    
    return quickSort(lewa) + [srodek] + quickSort(prawa)

mergeTime = []
quickTime = []
proby = 10
size = 50000 

for i in range(1, proby + 1):
    arr = generator(size)
    
    startTime = time.time()
    mergeSort(arr)
    stopTime = time.time()
    mergeTime.append(stopTime - startTime)

    startTime = time.time()
    quickSort(arr)
    stopTime = time.time()
    quickTime.append(stopTime - startTime)

plt.figure(figsize=(10, 6))
plt.plot(range(1, proby + 1), mergeTime, color='blue', label='Merge Sort')
plt.plot(range(1, proby + 1), quickTime,  color='red', label='Quick Sort')
plt.xlabel('Próba', fontsize=12)
plt.ylabel('Czas działania (s)', fontsize=12)
plt.legend(fontsize=12)
plt.grid(True)
plt.show()